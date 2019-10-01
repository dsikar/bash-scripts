from pointInfoReplyContent import PointInfoReplyContent;
from IDataFormatter import IDataFormatter;
from ByteCombinator import ByteCombinator;
from emptycontent import EmptyContent;


POINT_REPLY_EXPECTED_CONTENT_LENGTH = 42;

class PointReplyContentFormatter(IDataFormatter):
    """Class to format content bytes attatched to a packet id equal to point info reply (149)"""

    def format(self, replyBytes):
        Body = EmptyContent();
        #instance to call function that can take two 8 bit bytes and combine them into one 16 bit
        byteCombinator = ByteCombinator();

        if(len(replyBytes) > 1):
            if(len(replyBytes) == POINT_REPLY_EXPECTED_CONTENT_LENGTH):
                replyDict  =  {
                    'replyStatus'               : replyBytes[0],
                    'flags'                     : replyBytes[1],
                    'node'                      : replyBytes[2],
                    'channel'                   : replyBytes[3],
                    'channelAddress'            : replyBytes[4],
                    'pointCategory'             : replyBytes[5],
                    'pointNumber'               : replyBytes[6],
                    'logicalPointNumber'        : replyBytes[7],
                    'logicalPointZone'          : replyBytes[8],
                    'deviceType'                : replyBytes[9],
                    'auxiliaryPointAttr'        : replyBytes[10],
                    'group'                     : byteCombinator.combineBytes(replyBytes[11],replyBytes[12]),
                    'areaType'                  : replyBytes[13],
                    'areaNumber'                : replyBytes[14],
                    'sectorID'                  : replyBytes[15],
                    'loopType'                  : replyBytes[16],
                    'rawIdentity'               : replyBytes[17],
                    'actualDeviceType'          : replyBytes[18],
                    'mode&Sensitivity'          : replyBytes[19],
                    'rawAnalogueValue1'         : replyBytes[20],
                    'rawAnalogueValue2'         : replyBytes[21],
                    'rawAnalogueValue3'         : replyBytes[22],
                    'LTAFlags'                  : replyBytes[23],
                    'rawLTA'                    : replyBytes[24],
                    '%Dirtiness'                : replyBytes[25],
                    'unitofMeasure1'            : replyBytes[26],
                    'unitofMeasure2'            : replyBytes[27],
                    'unitofMeasure3'            : replyBytes[28],
                    'convertedValue1'           : replyBytes[29],
                    'convertedValue2'           : replyBytes[30],
                    'convertedValue3'           : replyBytes[31],
                    'instantaneousActiveState'  : replyBytes[32],
                    'instantaneousFaultState'   : replyBytes[33],
                    'confirmedActiveState'      : replyBytes[34],
                    'confirmedFaultState'       : replyBytes[35],
                    'acknowledgedActiveState'   : replyBytes[36],
                    'outputForcedMode'          : replyBytes[37],
                    'outputUnforcedState'       : replyBytes[38],
                    'outputForcedState'         : replyBytes[39],
                    'clientID'                  : byteCombinator.combineBytes(replyBytes[40] ,replyBytes[41]),
                    
                    };
                #2 sets of bytes have been combined thus the new expected length is 40
                Body = PointInfoReplyContent(**replyDict);
            else:
                raise TypeError("@PointInformationPacket: Invalid packet length");
        else:
            raise ValueError("@PointReplyContentFormatter: Point Info Reply formatter requires more than one byte");
        if(Body != None):
            return Body;

#For testing purposes replyBytes contains only content of a packet, it does not include SOH, FLG SIZE CHECKSUM OR HEADER
if(__name__ == '__main__'):

    #A length of 42 is used here to emulate a valid packet length as far as we have tested, 10 different test cases all the same content length
    #if the length is less than 42 or greater than but not equal to then for the time being it is raised as invalid content

    replyBytes = [0] * POINT_REPLY_EXPECTED_CONTENT_LENGTH;
    for index in range(1, len(replyBytes)):
        replyBytes[index] = index;

    body = PointReplyContentFormatter().format(replyBytes);

    print(body.getByteArray());