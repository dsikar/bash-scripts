
import  threading;
from    IDataTransfer import IDataTransfer, ITimableObject, ICancellable;
from    messaging import  Publisher, Subscriber;
from    messaging import Event as PyEvent;
from    packet import Packet;
import  packetids as  ids;
from    header import           LocalHeader ;
from    restartcontent import   RestartContent;
import  time;
from    serialdatatransfer import SerialDataTransfer;

MX_PROTOCOL_PORT_DATA_RECIEVED  = "mx.serial.port.data.recieved.event";
MX_PROTOCOL_SERIAL_READ_ERROR   = "mx.serial.port.read.error";
MX_SENDING__PACKET_EVENT        = "mx.sending.packet.event";
MX_TRANSPORT_PROTOCOL_CHANGED   = "mx.transport.protocol.changed";
THREAD_DAEMON_DELAY_TIMEOUT     = 2;
SOH           = 0x01
FLG           = 0x00 
ACK           = 0x06
MODULO        =  256

"""
 The protocol by default uses the PTP protocol to send packet via serial port(Transport");
"""
class Protocol(Publisher,Subscriber):
    
    def __init__(self , transport):
        Publisher.__init__(self);
        self.subscribe(self);
        self.__publishLocker       =  threading.Lock();
        self.__alive               =  False;
        self.__threadDeamon        =  threading.Thread(target= self.__run);
        self.__threadDeamon.daemon =  True;
        self.__transport           =  transport  if(isinstance(transport, IDataTransfer)) else  None;
        self.__writeLock           =  threading.Lock();
        self.__waitEvent           =  threading.Event();
        self.__sendFlag            =  FLG;

    @property
    def transport(self):
      return self.__transport;

   
    def setTransport(self, value):
      if(value != self.__transport):
        self.__transport = self.__transport;   
        if(self.__transport == None):
          self.alive = False;
        self.publish(PyEvent(MX_TRANSPORT_PROTOCOL_CHANGED, {"type":MX_TRANSPORT_PROTOCOL_CHANGED}));
       


    def onEvent(self, sender, event):
        playload   = event.playload;

        if(event.type  ==  MX_SENDING__PACKET_EVENT):
            #Packet and frame the packet that need to be send.
            self.onSendPacket(event);
        else:
          print(playload);
        pass;

    def publish(self, event):       
        with self.__publishLocker:
          self.__waitEvent.wait(THREAD_DAEMON_DELAY_TIMEOUT);
          if(self.alive == False):
            raise ValueError("@Protocol.publish: connection is not alive to be able to publish message");
          else:
            if(isinstance(event, PyEvent)) != True:
              raise ValueError("@Protocol.publish  taken an event type but unknown type given.");
          Publisher.publish(self, event);

    """******************************************************
    * @brief
    *   The method should be called by the thread class, instead of manually calling it.
    ******************************************************"""
    def __run(self):
        if(self.__transport != None):
           if(isinstance(self.__transport , ITimableObject)):
              self.__transport.setTimeout(1);
        error = None;
        self.__alive  = True;
        try:
          if(self.__waitEvent.is_set != True):
            self.__waitEvent.set(); # the only place where this event will be set.

            while ((self.__transport != None) and (self.alive == True and self.__transport.isConnected())):
              #Stop the loop immediate if anything goes wrong inside the protocol loop.
              if(error != None):
                   break;
              if(self.__transport.available):
                readData  =  self.__transport.Read();
                if(readData != ""):
                  #create an event to process the recieved data.
                  playload  =  {};
                  playload["data"]    = readData;
                  playload["length"]  = len(readData);
                  playload["type"]    = MX_PROTOCOL_PORT_DATA_RECIEVED;
                  event               =  PyEvent(MX_PROTOCOL_PORT_DATA_RECIEVED , playload);
                  self.publish(event);
        except Exception as err:
            playload  =  {};
            playload["type"]   = MX_PROTOCOL_SERIAL_READ_ERROR;
            playload["error"]  =  err;
            self.publish(playload);
            self.__stopListener();
       

    @property
    def alive(self):
       return self.__alive;

     #the function will start the protocol to listen and handle read event streaming.
    def start(self):
      if(self.alive == True):
            raise RuntimeError("@start has already be called on this object and protocol is already running.");
      self.__threadDeamon.start();


    def __stopListener(self):
       with self.__writeLock:  
        self.__alive = False;
        #all blocking event should finished up. 
        if(self.__transport != None):
          if(isinstance(self.__transport,ICancellable)):
              self.__transport.cancelRead();
              self.__transport.close();
        self.__threadDeamon.join(THREAD_DAEMON_DELAY_TIMEOUT);
        self.__waitEvent.set();
        

    def close(self):
        self.__stopListener();

    def send(self , packet):
      with self.__writeLock:
        if(isinstance(packet, Packet) != True):
          raise ValueError("@send: require parameter one to be a Packet type.");
        protocol.publish(PyEvent(MX_SENDING__PACKET_EVENT, packet));  


    def __sendPacket(self, packet):
      #frame the packet and send it.
        if(self.__transport != None):
           #write the packet to the transport.
            self.__transport.Write((SOH, self.__sendFlag, packet.size));
            packetBytes    = packet.getByteArray();
            self.__transport.Write(packetBytes);
            checksum = [self.__checksum(packet)];
            self.__transport.Write(checksum);
            self.__sendFlag = self.__sendFlag + 1;


    def __checksum(self, packet):
        global MODULO;
        checksum =  0       
        sum    = int(FLG)
        sum    += packet.size;
        bytes  =  packet.getByteArray();
        for data in bytes:
            sum   += data
        checksum   = sum % MODULO;
        return checksum;


    def __del__(self):
        self.close();
        del self.__threadDeamon;
        del self.__waitEvent;
        self.__threadDeamon = None;
        self.__waitEvent    = None;

    def onSendPacket(self, event):
       self.__sendPacket(event.playload);
       print("Packet {0} has be sent , size = {1}".format(event.playload.header.getParameter("packetID") , event.playload.size));



#Test packet protocol sending.
if(__name__ == "__main__"):
    protocol  =    Protocol(SerialDataTransfer("COM1"));
    protocol.start();
   
    for i in range(0,5):
      protocol.publish(PyEvent("initial.event", {"name":"Obaro"})); 
      #Sending packet  using the protocol.
      header   =  LocalHeader(ids.spkd_ID_RESTART_REQUEST);
      reset    =  RestartContent();
      packet   =  Packet(header,reset);
      protocol.publish(PyEvent(MX_SENDING__PACKET_EVENT, packet));  

    protocol.setTransport(None);
   
    protocol.close();
    


 


