"""
 The module file contain the PTP byte reader from the commport 
 
"""
""" ****************************************************************************
*@brief
*  The abstract class provided IDataFormatter interface 
*  for taking a string of bytes and parse it into a packet.
**************************************************************************** """
import threading;
from IDataTransfer import IDataTransfer;
from serialdatatransfer import SerialDataTransfer;
from frame import SOH, ACK;
from ByteBuffer import ByteBuffer;
from byte import Byte;
from messaging import Event, Publisher;


INVALID_PACKET_START_BYTE  = 0x01;
READ_THREAD_DELAY_TIMEOUT  = 5;
INVALID_CHAR               = '\x00';
TRANSPORT_READ_TIMEOUT     = 0x02;
DATA_READER_EVT_READ   ='serial.read.event'

class IDataReader:
    
    def Read(self , bytes):
        raise NotImplementError("@IDataReader format function needs to be implemented.");

class IHaveDataTransfer:

    def GetDataTransfer(self):
        raise NotImplementError("@IHaveDataTransfer format function needs to be implemented.");

class IErrorMessage:
    def GetLastError(self):
        raise NotImplementError("@IHaveDataTransfer format function needs to be implemented.");
    def GetErrorCode(self):
        raise NotImplementError("@IHaveDataTransfer format function needs to be implemented.");

class IStartableObject:
    def Start(self):
         raise NotImplementError("@IStartableObject must be implemented");

"""
Custom exception for the data reader class.
"""
class BadPacketReadError(Exception):
    def __init__(self, err , errorBytes, code ):
         Exception.__init__(self, err);
         self.__bytes  = errorBytes;
         self.__code   = code;
    def getArrayBytes(self):
       return self.__bytes ;

    def __str__(self):
        return '{0},code={1}'.format(self.message, self.__code);


"""
    Data Reader Implementation
"""
class DataReader(IDataReader,IErrorMessage, IStartableObject, Publisher):

    def __init__(self, dataTransfer):
        if(isinstance(dataTransfer,IDataTransfer) != True):
            raise ValueError("@DataReader : expecting parameter one to be IDataTransfer object");
        self.__dataTransfer =  dataTransfer;
        self.__rxQueue      = ByteBuffer();
        self.__rxThread     = threading.Thread(target=self.__RunInBackground, name="mxDataReader" , args=(self.__rxQueue, ));
        self.__rxThread.daemon = True;
        self.__waitEvent    =  threading.Event();
        self.__waitTaskCompleted   =  threading.Event();
        self.__isAlive      = False;
        self.__mutex        = threading.Lock();


    def IsRunning(self):
        return  ((self.__dataTransfer != None) and 
                 (self.__dataTransfer.IsConnected()) and 
                 self.__isAlive);

    def __del__(self):
      if( self.__rxThread != None):
          self.__rxThread.join(READ_THREAD_DELAY_TIMEOUT);
          pass;
      self.__rxThread = None;
      self.__waitEvent = None;


    def GetLastError(self):
        return self.__errorCode;

    def Start(self):
        if(self.IsRunning() != True):
            if(self.__rxThread.isAlive() != True):
              self.__rxThread.daemon = True;
              self.__waitTaskCompleted.clear();
              self.__waitEvent.clear();
              self.__rxThread.start();
       

    def __RunInBackground(self, SeqQueue):
        if(self.__isAlive != True):
            self.__error = None;
            if(self.__waitEvent.is_set != True):
                 self.__waitEvent.set();
                 self.__isAlive = True;
               
                 while(self.IsRunning()):
                     try:
                         if(self.__error != None):
                              break;
                         if((self.__dataTransfer != None) and (self.__dataTransfer.IsDataAvailable())):
                             self.__rxQueue.put(self.__dataTransfer.Read());
                     except Exception as err:
                        self.__error  = err;
                        print(self.__error);

            self.__isAlive   = False;
            self.__waitTaskCompleted.set();


    def IsDataAvailable(self):
       return (self.__rxQueue.empty() != True);
    
    def __isStartByte(self, byte):
        sbyte  =  ord(byte);
        return ( (sbyte == ACK) or (sbyte == SOH));

    """
     The function will handle an event packet errors.
    """
    def _GetInvalidBytes(self,  argbytes):
         bytes  =  bytearray();

         for byte in argbytes:
           bytes.append(byte);

         while(self.__rxQueue.empty() != True):
            byte  = self.__rxQueue.peek(0);
            if(byte != None):
                if(self.__isStartByte(byte)):
                     break;
            byte = self.__rxQueue.get();
            bytes.append(byte);
         return bytes;
       
    def Stop(self):      
       if(self.IsRunning()):
         try:
            self.__isAlive = False;    
            if(self.__waitTaskCompleted != None):
               self.__waitTaskCompleted.wait();   
            if(self.__rxThread != None):
              self.__rxThread.join(READ_THREAD_DELAY_TIMEOUT)
         except Exception as err:
           print(err);
         finally:
             self.__rxThread = None;

       return (self.__rxThread == True);
                  
           

    """*********************************************
    *@brief
    * The function will read the current packet bytes from 
    * The queue , return ACK if
    *  throw an exception if invalid packet is read.
    *  throw an exception for incompleted bytes.
    *********************************************"""
    def Read(self):
        bytes  = bytearray();
        with self.__mutex: 
           if(self.IsDataAvailable()):
                continueWith  = True;
                try:
                    if(self.IsRunning() == True):
                        byte = self.__rxQueue.get();
                        if(self.__isStartByte(byte)):
                             bytes.append(byte);

                             if(ord(byte) == SOH):
                                 byte = self.__rxQueue.get(True, READ_THREAD_DELAY_TIMEOUT);
                                 bytes.append(byte);
                                 byte = self.__rxQueue.get(True, READ_THREAD_DELAY_TIMEOUT);
                                 pLength  = ord(byte);
                                 bytes.append(byte);

                                 for index in range(0, pLength):
                                     byte =  self.__rxQueue.get(True, READ_THREAD_DELAY_TIMEOUT);
                                     bytes.append(byte);
                        else:
                            bytes =  self._GetInvalidBytes(byte);
                            raise (BadPacketReadError("Invalid start byte read.",bytes,INVALID_PACKET_START_BYTE));
                               
                except Exception as err:
                        bytes = self._GetInvalidBytes(bytes);
                        raise BadPacketReadError(err.message,bytes,TRANSPORT_READ_TIMEOUT);
        return bytes;

    def Wait(self):
      if(self.__waitEvent != None):
        self.__waitEvent.wait();



"""
 CODE TESTING HERE
"""
reader = None;
import struct;
def read(reader, nPackets):
    reader.Wait();
    status = False;
    count =   0;
    while(reader.IsRunning() ):
        try:
            data = reader.Read();
            if(len(data)>0):
               for index in range(0 , len(data)):
                   item  = data[index];
                   print('D+{0} =  {1}\n'.format(index, Byte(item)));
               if(nPackets == count):
                    reader.Stop();
                    count = 0;
               count = count + 1;
              
        except BadPacketReadError as err:
            print err;
            
    return  status;     

def start(reader):
      reader.Start();
#1 1 52 0 0 0 0 0 4 0 149 1 32 0 0 0 255 255 253 254 128 0 0 1 3 255 254 7 0 128 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 240
if(__name__ =='__main__'):
    reader  = DataReader(SerialDataTransfer('COM8'));
    start(reader);
    read(reader , 8);
    print("Hello World");
# 0x00,0x00,0x00, 0x06