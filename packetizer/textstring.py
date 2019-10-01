
from content import Content;

class TestStringContent(Content):

    def __init__(self , **kwargs):

        params  = {
              "type"                        : 0x00,
              "channel"                     : 0x00,
              "channelAddress"              : 0x00,
              "pointCategory"               : 0x00,
              "pointNumber"                 : 0x00,
              "logicalPointAddress"         : 0x00,
              "logicalPointZone"            : 0x00,             
              "zoneNumber"                  : 0x00,
              "panelNumber"                 : 0x00, # 0 - 99
              "informationTextID"           : 0x00  # 1 -100
            };

        for key in kwargs:
            if(key in params) != True:
                raise ValueError("".format("@TestStringContent: invalid parameter given {0}", key));
            params[key] =  kwargs[key];
        Content.__init__(self, **params);




        def getByteArray(self):
            requestType = self.toBitArray(self.getParameter("type"), True);
            #Bit0=Point Text Requested
            #Bit1=Zone Text Requested
            #Bit3=Reserved for future use
            #Bit4=Info Text Requested
            #Bit7=Strings are requested in Secondary Language

            if(requestType[0] == True):
                #create the packet bytes needed.
                pass;
           
            if(requestType[1] == True):
                #create the packet bytes needed.
                pass;
           
            if(requestType[2] == True):
                #create the packet bytes needed.
                pass;
          
            if(requestType[4] == True):
                #create the packet bytes needed.
                pass;

            
            if(requestType[4] == True):
                #create the packet bytes needed.
                pass;
            
            

            return data;

