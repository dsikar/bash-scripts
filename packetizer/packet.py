
from header    import Header;
from content   import Content, ByteContainer;

#List OF All Supported MX packets.
"""***************************************************
*
*
***************************************************"""

class Packet(ByteContainer):
    def __init__(self, header, content):
        if(isinstance(header ,Header) != True):
            raise AttributeError("header object must be a type of packets.Header");
        if(isinstance(content, Content) != True):
            raise AttributeError("@content: must be of type packets.Content");
        self.__header   =  header;
        self.__content  =  content;
    
    def getByteArray(self):
        headerData        =  self.__header.getByteArray();
        contentData       =  self.__content.getByteArray();
        if(isinstance(headerData, list)) != True:
            raise AssertionError("@Packet.Header.getByteArray : must return a bytes array object list.");
        if(isinstance(contentData, list)) != True:
            raise AssertionError("@Packet.Content.getByteArray : must return a bytes array object list.");
      
        return (headerData + contentData)

    @property
    def header(self):
        return self.__header;

    @property
    def content(self):
        return self.__content;

    def count(self):
        length  =  len(self.getByteArray());
        return length + 1;

    @property
    def size(self):
        return self.count();