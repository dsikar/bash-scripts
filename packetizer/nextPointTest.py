from pointinformationcontent import *;
from nextPointInformationContent import NextPointInformationContent;
from LocalFrameFormatter import LocalFrameFormatter;
from header import LocalHeader;
from content import Content;
from packet import Packet;
from frame import Frame;   

from serialdatatransfer import SerialDataTransfer;
from readers import DataReader, BadPacketReadError;
from byte import Byte;

import packetids as packetID;

import time;

ResultFrame = LocalFrameFormatter();

class NextPointInformationTest:
    """class to construct and test the point information packet using speak 6 header"""
    global ResultFrame;
    ResultFrame = LocalFrameFormatter();

    global FLG;
    FLG = 0x00;

    def createPointInformationPacket(self):
        """function to build a point information request packet using speak 6 header"""

        header = LocalHeader(packetID.spkd_ID_POINT_INFO_REQUEST);
        header.setParameter("destinationTask", 0x04);
        header.setParameter("sourceChannelAddress", 0xFD); #values sent by consys for header replicated here
        header.setParameter("sourceTask",0x92);

        content  =  PointInformationContent();
        content.setParameter("searchType", 0x0A);
        packet   =  Packet(header, content);
        frame    =  Frame(packet, FLG);

        header.IgnoreReserved(True);
        
        transfer.Write(frame.getByteArray());

        print(frame.getByteArray());
        print("Point Information Reply Packet"); 

    def sendNextPointInformationPacket(self,clientID):
        global FLG;
        header = LocalHeader(packetID.spkd_ID_POINT_CLNT_ACKNOWLEDGE);
        header.setParameter("destinationTask",0x04);
        header.setParameter("sourceChannelAddress",0xFD);
        header.setParameter("sourceTask",0x12);

        FLG = FLG + 1;
        content = NextPointInformationContent();
        content.setParameter("clientID",clientID);
        packet   =  Packet(header, content);
        frame    =  Frame(packet, FLG);

        header.IgnoreReserved(True);

        transfer.Write(frame.getByteArray());
   
        print(frame.getByteArray());
        print("Next Point Information Reply\n");


def read(reader, transfer):
    global ResultFrame;

    packetObject = NextPointInformationTest();
    packetObject.createPointInformationPacket();

    while(True):
        try:
            data = reader.Read();
            if(len(data) > 0):

               for index in range(0, len(data)):
                  item  = data[index];
                  print('D+{0} =  {1}'.format(index, Byte(item)));
     
               if(len(data) > 1):
                   transfer.Write([0x06]);
                   ResultFrame = ResultFrame.format(data);  #format data
                   clientID = ResultFrame.packet.content.getParameter("clientID"); #get contentparam from packet
                   ResultFrame = LocalFrameFormatter();     #create new FrameFormatter instance
                   packetObject.sendNextPointInformationPacket(clientID);   #send nextpoint with client id of point reply
            
        except BadPacketReadError as err:
            print("Error Bytes");
            bytes  =  err.getArrayBytes();
            for index in range(0 , len(bytes)):
                  item  = bytes[index];
                  print('D+{0} =  {1}\n'.format(index, Byte(item)));
            print err;

if(__name__ == '__main__'):

    transfer = SerialDataTransfer("COM20");

    reader   = DataReader(transfer);
    reader.Start();

    read(reader,transfer);


