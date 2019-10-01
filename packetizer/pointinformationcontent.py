from content import Content;
import devicetype as devices;
from ByteCombinator import ByteCombinator;

class PointCategoryType:
    padr_PCAT_REAL        = 0x00;
    padr_PCAT_PSEUDO      = 0x01;
    padr_PCAT_XBUS        = 0x02;
    padr_PCAT_TIMER       = 0x03;
    padr_PCAT_MENU        = 0x04;
    padr_PCAT_ISOLATE     = 0x05;
    padr_PCAT_USER        = 0x06;
    padr_PCAT_FOREIGN     = 0x07;
    padr_NUM_OF_PT_CATEGS = 0x08;
    padr_PCAT_LAST        = 0x08 - 1,
    padr_PCAT_FIRST       = 0,
    padr_PCAT_NOT_A_POINT = 0xFE,      
    padr_PCAT_ALL         = 0xFF,

class DeviceCategoryType:
    ALL_DEVICE_TYPE       = 0x00;
    INPUT_DEVICE_TYPE     = 0x01;
    OUTPUT__DEVICE_TYPE   = 0x02;
    CALLPOINT_DEVICE_TYPE = 0x03;

class PointSearchType:
    POINT_WITH_INPUT_ISOLATOR  = 0x00;
    POINT_WITH_OUTPUT_ISOLATOR = 0x01;
    ALL_POINTS                 = 0x0A;
    ACTIVE_INPUTS              = 0x1C;

class ChannelType:
     LOCAL_IO_TYPE   =  0x00; 
     MP_DIGITAL_TYPE =  0x0D;
     MX_LOOP_TYPE    =  0x0C;
class MultiAreaType:
    ALL  =  0x03 ; #I dont care


class PointInformationContent(Content):
    """Class to populate content for point information packet"""

    def __init__(self, **kwargs):

          attributes  =  {
               'panelNumber'           : 0x00, 
               'channel'               : ChannelType.MX_LOOP_TYPE,
               'loopNumber'            : 0xFF,  
               'pointCategory'         : PointCategoryType.padr_PCAT_REAL,
               'pointNumber'           : 0xFF, 
               'logicalPointNumber'    : 0xFD, 
               'logicalPointZone'      : 0xFE,
               'deviceCategory'        : DeviceCategoryType.ALL_DEVICE_TYPE,
               'group'                 : ByteCombinator().combineBytes(0x00, 0x01), #Two Bytes
               'outputPointStoreState' : 0x03,
               'reserved1'             : 0x00, 
               'reserved2'             : 0x00, 
               'multiAreaType'         : MultiAreaType.ALL,
               'areas'                 : Content.createSizeArray(29, 0xFF),
               'area'                  : 0xFF,
               'reserved'              : 0x01,
               'deviceType'            : devices.pdev_DEVICE_ID_ALL,
               'requestType'           : 0x01,
               'searchType'            : PointSearchType.ACTIVE_INPUTS
              };

          for key in kwargs:
              if ((key in attributes) != True):
                raise ValueError(key);
              attributes[key]=  kwargs[key];
          Content.__init__(self, **attributes);

    def getByteArray(self):
        bytes  = Content.createSizeArray(14, 0x00);
        bytes[0]  = self.getParameter("panelNumber");
        bytes[1]  = self.getParameter("channel");
        bytes[2]  = self.getParameter("loopNumber");
        bytes[3]  = self.getParameter("pointCategory");
        bytes[4]  = self.getParameter("pointNumber");
        bytes[5]  = self.getParameter("logicalPointNumber");
        bytes[6]  = self.getParameter("logicalPointZone");
        bytes[7]  = self.getParameter("deviceCategory");
        bytes[8]  = self.getLSB(self.getParameter("group"));
        bytes[9]  = self.getMSB(self.getParameter("group"));
        bytes[10]  = self.getParameter("outputPointStoreState");
        bytes[11]  =  self.getParameter("reserved1");
        bytes[12]  =  self.getParameter("reserved2");
        bytes[13]  = self.getParameter("multiAreaType");

        for value in self.getParameter('areas'):
            bytes.append(value);

        bytes.append(self.getParameter("area"));
        bytes.append(self.getParameter("reserved"));
        bytes.append(self.getParameter("deviceType"));
        bytes.append(self.getParameter("requestType"));
        bytes.append(self.getParameter("searchType"));
        return bytes;