from packet import Packet;
from threading import Lock;
from header import LocalHeader, NetworkHeader, LOCAL_HEADER, NETWORK_HEADER;    
from content import Content;

class Registry:

    def register(self, value):
        pass;
    def unregister(self, value):
        pass;
    def get(self, key):
        pass;
    def count(self):
        return  0;

class PacketRegistry:
    __registryInstance  =  None;
    __lockInstance      = Lock();

    @staticmethod
    def createPacket(packetid, headerType= LOCAL_HEADER):
        packetid  =  packetid if (type(packetid) == int) else None;
        #Check if packet exists
        if(PacketRegistry.__registryInstance == None):
           PacketRegistry.__registryInstance = PacketRegistry.getInstance();
        if(PacketRegistry.__registryInstance.exists(packetid)) != True:
            raise AssertionError("@createPacket : Packet({0}) is not found in registry".format(packetid));
        content   = PacketRegistry.__registryInstance.get(packetid);
        packetObject = None;

        if(content != None):
            contentObject   = content();
            CurrentHeader   = LocalHeader  if(headerType != NETWORK_HEADER) else NetworkHeader;
            packetObject    = Packet(CurrentHeader(packetid), contentObject);       
        return  packetObject;

    @staticmethod
    def getInstance():
        PacketRegistry.__lockInstance.acquire();
        if( PacketRegistry.__registryInstance  == None):
            PacketRegistry.__registryInstance = PacketRegistry.__PacketRegistry();
        PacketRegistry.__lockInstance.release();
        return PacketRegistry.__registryInstance;

    """**************************************************************************
    * @brief
    *  The class will managed the packet objects.
    *
    **************************************************************************"""
    class __PacketRegistry(Registry):
        def __init__(self):
            self.__contents  =  dict();
            pass;

        def get(self, key):
            packet  = None;
            if(key in self.__contents):
                packet = self.__contents[key];
            return packet;

        def register(self , key , content):
            if(self.__keyExists(key)) != True:
               self.__contents[key] = content;
            return self;

        def unregister(self, key):
            if  key in  self.__contents:
                del self.__contents[key];
            return self;

        def exists(self, key):
            return self.__keyExists(key);
      
        def __keyExists(self, key):
            found = False;
            if  key in  self.__contents:
                found  = True;
            return found;

        def count(self):
            return len(self.__contents);

         
  
    