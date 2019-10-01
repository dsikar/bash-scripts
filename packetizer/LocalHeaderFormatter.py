from IDataFormatter import IDataFormatter;
from header   import LocalHeader, NetworkHeader;
""" ****************************************************************************
*@brief
*  The class is provided for parsing the bytes for Local Header
*  Input: the header bytes
*  Output: the header
**************************************************************************** """
class LocalHeaderFormatter(IDataFormatter):
    def format(self , bytes):
        header = None;
        if(len(bytes) == 10):
            header  = LocalHeader(bytes[8]);
            header.setParameter("signature",bytes[0]);
            header.setParameter("networkNode",bytes[1]);
            header.setParameter("channel",bytes[2]);
            header.setParameter("destinationChannelAddress",bytes[3]);
            header.setParameter("destinationTask",bytes[4]);
            header.setParameter("sourceChannelAddress",bytes[5]);
            header.setParameter("sourceTask",bytes[6]);
            header.setParameter("marker",bytes[7]);
            header.setParameter("reserved",bytes[9]);
        else:
            raise ValueError("@LocalHeaderFormatter: the bytes length is unvalid");
        return header;
#test header code here
if(__name__ == '__main__'):
    bytes = [1,2,3,4,5,6,7,8,9,10];
    header = LocalHeaderFormatter().format(bytes);
    print(len(bytes));   #10
    print(type(bytes));  #list
    print(bytes[5]);   #6
    print( header.getParameter("packetID"));  #9
    print( header.getParameter("reserved"));  #10
