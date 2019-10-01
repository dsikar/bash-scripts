
from content import Content;

MX_SIGNATURE    = 0xE4 #228
LOCAL_HEADER    = 0x01;
NETWORK_HEADER  = 0x02;


"""************************************************************************************************************************************
* @brief
*  The funciton will make contain the fixed size bytes required by the MX protocol.
************************************************************************************************************************************"""
class Header(Content):
     def __init__(self, **kwargs):
         Content.__init__(self, **kwargs);


"""************************************************************
* The Local Header is used when the port on the panel is COM2
************************************************************"""
class LocalHeader(Header):

    def __init__(self, packetid):
        params  =  {
            "signature"                         : MX_SIGNATURE,
            "networkNode"                       : 0x00,
            "channel"                           : 0x00,
            "destinationChannelAddress"         : 0x00,
            "destinationTask"                   : 0x00,
            "sourceChannelAddress"              : 0x00,
            "sourceTask"                        : 0x00,
            "marker"                            : 0x00,
            "packetID"                          : packetid,
            "reserved"                          : 0x00
          };
        self.__reservedNeeded = False;
        Header.__init__(self, **params);

    @property
    def getIgnoreReserved(self):
        return self.__reservedNeeded;

    def IgnoreReserved(self, value):
       if(self.__reservedNeeded != value):
          self.__reservedNeeded  = value;
     
    def getByteArray(self):

        if(self.getIgnoreReserved != True):
            length = self.count();
        else:
            length = self.count() - 1;

        data    =  self.createSizeArray(length , 0);
        data[0]  = self.getParameter("signature");
        data[1]  = self.getParameter("networkNode");
        data[2]  = self.getParameter("channel");
        data[3]  = self.getParameter("destinationChannelAddress");
        data[4]  = self.getParameter("destinationTask");
        data[5]  = self.getParameter("sourceChannelAddress");
        data[6]  = self.getParameter("sourceTask");
        data[7]  = self.getParameter("marker");
        data[8]  = self.getParameter("packetID");
        if(self.getIgnoreReserved != True):
            data[9]  = self.getParameter("reserved");
        return data;


class LocalHeader5(Header):
    def __init__(self, packetid):
        params  =  {
            "networkNode"                      : 0x00,
            "channel"                          : 0x00,
            "destinationChannelAddress"        : 0x00,
            "destinationTask"                  : 0x00,
            "sourceChannelAddress"             : 0x00,
            "sourceTask"                       : 0x00,
            "marker"                           : 0x00,
            "packetID"                         : packetid
          };

    def getByteArray(self):
        data    =  self.createSizeArray(self.count() , 0);
        data[0]  = self.getParameter("networkNode");
        data[1]  = self.getParameter("channel");
        data[2]  = self.getParameter("destinationChannelAddress");
        data[3]  = self.getParameter("destinationTask");
        data[4]  = self.getParameter("sourceChannelAddress");
        data[5]  = self.getParameter("sourceTask");
        data[6]  = self.getParameter("marker");
        data[7]  = self.getParameter("packetID");

"""************************************************************
* This is the header required when COM3 is used in the panel to
*  send the command.
*
************************************************************"""
class NetworkHeader(Header):

    def __init__(self, packetid):
        params  =  {
            "signature"                         : MX_SIGNATURE,
            "destinationNode"                   : 0x00,
            "sourceNode"                        : 0x00,
            "packetID"                          : packetid,
            "destinationPortChannel"            : 0x00,
            "destinationPortChannelAddress"     : 0x00,
            "destinationTask"                   : 0x00,
            "sourcePortChannel"                 : 0x00,
            "sourcePortChannelAddress"          : 0x00,
            "sourceTask"                        : 0x00,
            "marker"                            : 0x00,
            "reserved"                          : 0x00
          };
        Header.__init__(self, **params);

    def getByteArray(self):
        data    =  self.createSizeArray(self.count(), 0x00);
        data[0]  = self.getParameter("signature");
        data[1]  = self.getParameter("destinationNode");
        data[2]  = self.getParameter("sourceNode");
        data[3]  = self.getParameter("packetID");
        data[4]  = self.getParameter("destinationPortChannel");
        data[5]  = self.getParameter("destinationPortChannelAddress");
        data[6]  = self.getParameter("destinationTask");
        data[7]  = self.getParameter("sourcePortChannel");
        data[8]  = self.getParameter("sourcePortChannelAddress");
        data[9]  = self.getParameter("sourceTask");
        data[10] = self.getParameter("marker");
        data[10] = self.getParameter("reserved");
        return data;