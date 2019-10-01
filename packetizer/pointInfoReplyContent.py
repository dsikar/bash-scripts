from content import Content;

EXPECTED_CONTENT_SIZE = 40;

class PointInfoReplyContent(Content):

    def __init__(self, **kwargs):
        if(len(kwargs) != EXPECTED_CONTENT_SIZE):
            raise TypeError("@PointInfoReplyContent: Insufficient number of paramaters provided");
        else:
            Content.__init__(self, **kwargs);

    def getByteArray(self):
        bytes = Content.createSizeArray(42, 0x00);

        bytes[0] = self.getParameter("replyStatus");
        bytes[1] = self.getParameter("flags");
        bytes[2] = self.getParameter("node");
        bytes[3] = self.getParameter("channel");
        bytes[4] = self.getParameter("channelAddress");
        bytes[5] = self.getParameter("pointCategory");
        bytes[6] = self.getParameter("pointNumber");
        bytes[7] = self.getParameter("logicalPointNumber");
        bytes[8] = self.getParameter("logicalPointZone");
        bytes[9] = self.getParameter("deviceType");
        bytes[10] = self.getParameter("auxiliaryPointAttr");
        bytes[11] = self.getLSB(self.getParameter("group"));
        bytes[12] = self.getMSB(self.getParameter("group"));

        bytes[13] = self.getParameter("areaType");
        bytes[14] = self.getParameter("areaNumber");
        bytes[15] = self.getParameter("sectorID");
        bytes[16] = self.getParameter("loopType");
        bytes[17] = self.getParameter("rawIdentity");
        bytes[18] = self.getParameter("actualDeviceType");
        bytes[19] = self.getParameter("mode&Sensitivity");
        bytes[20] = self.getParameter("rawAnalogueValue1");
        bytes[21] = self.getParameter("rawAnalogueValue2");
        bytes[22] = self.getParameter("rawAnalogueValue3");
        bytes[23] = self.getParameter("LTAFlags");
        bytes[24] = self.getParameter("rawLTA");
        bytes[25] = self.getParameter("%Dirtiness");

        bytes[26] = self.getParameter("unitofMeasure1");
        bytes[27] = self.getParameter("unitofMeasure2");
        bytes[28] = self.getParameter("unitofMeasure3");
        bytes[29] = self.getParameter("convertedValue1");
        bytes[30] = self.getParameter("convertedValue2");
        bytes[31] = self.getParameter("convertedValue3");
        bytes[32] = self.getParameter("instantaneousActiveState");
        bytes[33] = self.getParameter("instantaneousFaultState");
        bytes[34] = self.getParameter("confirmedActiveState");
        bytes[35] = self.getParameter("confirmedFaultState");
        bytes[36] = self.getParameter("acknowledgedActiveState");
        bytes[37] = self.getParameter("outputForcedMode");
        bytes[38] = self.getParameter("outputUnforcedState");
        bytes[39] = self.getParameter("outputForcedState");
        bytes[40] = self.getLSB(self.getParameter("clientID"));
        bytes[41] = self.getMSB(self.getParameter("clientID"));
    
        return bytes;