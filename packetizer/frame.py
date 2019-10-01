"""*********************************************************************************
*  @author (Obaro)
*  @date   (07 September 2018).
*  @description
*   The file contains the implementation of the PTP frame data link layer.
*********************************************************************************"""

from  packet  import Packet;
from  header   import LocalHeader, NetworkHeader, LOCAL_HEADER, NETWORK_HEADER;    


SOH           = 0x01
FLG           = 0x00 
ACK           = 0x06
MODULO        =  256


"""
The PTP Frame
"""
class Frame:

    def __init__(self, packetObject, flgbyte):
        if(isinstance(packetObject, Packet)) != True:
             raise ValueError("@Require parameter one to be a packet object");

        self.__packet         =  packetObject;
        self.__flgbyte          =  flgbyte;
        pass;

    """*****************************************
    * @brief
    *  The function will prepare and get the bytes array 
    *****************************************"""
    def getByteArray(self):
        bytes   =  list();
        bytes   += [SOH, self.__flgbyte, self.__packet.size];
        bytes   += self.__packet.getByteArray();
        bytes   += [self.checksum(self.__packet)];
        return bytes;

    @property
    def packet(self):
        return self.__packet;

    def setContent(self, key, value):
       if(isinstance(key , basestring)):
           self.__packet.content.setParameter(key, value);

    def setHeader(self, key, value):
          if(isinstance(key , basestring)):
              self.__packet.header.setParameter( key, value);
   
    def count(self):
        bytes  =  self.getByteArray();
        return len(bytes);

    def checksum(self, packet):
        global MODULO;
        if(isinstance(packet, Packet) != True):
            raise AttributeError("@DataCheckable : Parameter must be a type packets.Packet");
        if(self.__flgbyte == None):
            self.__flgbyte = FLG;
        checksum =  0       
        sum    = int(self.__flgbyte);
        sum    += packet.size;
        bytes  =  packet.getByteArray();

        for data in bytes:
            sum   += data
        checksum   = sum % MODULO;
        return checksum;