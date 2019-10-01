from content import Content;
from header import LocalHeader, LocalHeader5;
from packetids import spkd_ID_POINT_INFO_REQUEST;
from packet import Packet;
import devicetype as devices;
from frame import Frame;   
from serialdatatransfer import SerialDataTransfer;
from readers import DataReader, BadPacketReadError;
from byte import Byte;
from points import *;

if(__name__ == '__main__'):
    header   = LocalHeader(spkd_ID_POINT_INFO_REQUEST);
    header.setParameter("destinationTask", 0x04);
    header.setParameter("sourceChannelAddress", 0xfd);
    header.setParameter("sourceTask",0x92);
    content  =  PointInformationContent();
    content.setParameter('PanelNumber', 0x0c);
    content.setParameter('Channel', 0xff);
    content.setParameter('LoopNumber', 0x00);
    content.setParameter('PointCategory', 0xff);
    content.setParameter('PointNumber', 0xfd);
    content.setParameter('LogicalPointNumber', 0xfe);
    content.setParameter('LogicalPointZone', 0x00);
    content.setParameter('DeviceCategory', 0x00);
    content.setParameter('Group', 0x01);
    content.setParameter('LogicalPointZone', 0x00);
    content.setParameter('LogicalPointZone', 0x00);
    content.setParameter('LogicalPointZone', 0x00);
    packet   =  Packet(header, content);
    frame    =  Frame(packet , 0x0d);
    print( frame.getByteArray());



