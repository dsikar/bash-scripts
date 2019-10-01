from pointinformationcontent import *;
from header import LocalHeader;

from content import Content;
from packet import Packet;
from frame import Frame;   

from serialdatatransfer import SerialDataTransfer;
from readers import DataReader, BadPacketReadError;
from byte import Byte;

import packetids as packetID;
import devicetype as devices;

class PointInfoPacketConstruction:
    """class to construct and test the point information packet using speak 6 header"""

    global FLG;
    FLG = 0x00;

    def createPointInformationPacket(self):
        """function to build a point information request packet using speak 6 header"""

        header = LocalHeader(packetID.spkd_ID_POINT_INFO_REQUEST);
        header.setParameter("destinationTask", 0x04);
        header.setParameter("sourceChannelAddress", 0xFD); #values sent by consys for header replicated here
        header.setParameter("sourceTask",0x92);

        header.IgnoreReserved(True);

        content  =  PointInformationContent();
        packet   =  Packet(header, content);
        frame    =  Frame(packet, FLG);

        transfer = SerialDataTransfer("COM20");
        reader   = DataReader(transfer);
        reader.Start();#executes read thread to process incoming response after sent request
        transfer.Write(frame.getByteArray());
   
        print(frame.getByteArray());
        print("Point Information Reply\n");
        
        read(reader,transfer);

def read(reader, transfer):

    #Responsible for preventing endless rx thread loop
    LoopControl = True;
    while(LoopControl):
        try:
            data = reader.Read();

            if(len(data) > 0):
               for index in range(0, len(data)):
                    item  = data[index];
                    print('D+{0} =  {1}'.format(index, Byte(item)));
                    
               if(len(data) > 1):
                   transfer.Write([0x06]);
                   LoopControl = False;
     
        except BadPacketReadError as err:
            print("Error Bytes");
            bytes  =  err.getArrayBytes();
            for index in range(0 , len(bytes)):
                  item  = bytes[index];
                  print('D+{0} =  {1}\n'.format(index, Byte(item)));
            print err;

        if(LoopControl == False):
           reader.__del__();

if(__name__=='__main__'):

    packetObject = PointInfoPacketConstruction();
    packetObject.createPointInformationPacket();

    



