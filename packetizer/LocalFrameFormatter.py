
from IDataFormatter import IDataFormatter;
from LocalHeaderFormatter import LocalHeaderFormatter;
from ResetContentFormatter import ResetContentFormatter;
from PointReplyContentFormatter import PointReplyContentFormatter;
from LoopControlRequestFormatter import LoopControlRequestFormatter;
from frame import Frame;
from   emptycontent import EmptyContent;
import packetids as id;
from   packet   import Packet;
""" ****************************************************************************
*@brief
*  The class is provided for parsing the whole input bytes, dividing the bytes 
*into header and body parts, checking the type of the body, 
*calling the LocalHeaderFormatter and ResetContentFormatter function to parse 
*each part as well as packet and return the header and the body.
*  Input: the whole input bytes.
*  Output: the packet object with the header and the body in it.
**************************************************************************** """
class LocalFrameFormatter(IDataFormatter):

    """
    * @brief
    *  The function will get the current playload object for the ID.
    """
    def __getCurrentPayloadObject(self, packetID, Bytes):
       payload = EmptyContent();

       if(packetID == id.spkd_ID_RESTART_REQUEST):
            payload = ResetContentFormatter().format(Bytes);
       elif(packetID == id.spkd_ID_LOOP_SHUTDOWN_RESTART):
             payload = LoopControlRequestFormatter().format(Bytes);
       elif(packetID == id.spkd_ID_POINT_INFO_REPLY):
           payload = PointReplyContentFormatter().format(Bytes);
       else:
           raise ValueError("@LocalFrameFormatter: Formatter for this packet does not exist yet");
       return payload;

    """
      Call to get the current object of the  bytes provided.
      We are using speak 6 header here
    """
    def format(self, bytes):
        payload   = None;
        header     = None;
        if( (type(bytes) == list) or (type(bytes) == bytearray)):
            if (len(bytes) >= 14):
                headerBytes  =  bytes[3:13]
                header  = LocalHeaderFormatter().format(headerBytes)
                if (header == None):
                     raise ValueError("@LocalFrameFormatter: the header is empty!")
                else: 
                    if (len(bytes) > 14): 
                        tempBodyBytes = len(bytes) - 1;
                        BodyBytes     = bytes[13:tempBodyBytes];
                        payload       = self.__getCurrentPayloadObject(header.getParameter("packetID"),  BodyBytes);
            else: 
                raise ValueError("@LocalFrameFormatter: The length of bytes is not enough!");
        else:
            raise ValueError("@LocalFrameFormatter: Require List object of bytes");
        #At this point the header is not none and the body can be emptycontent or a real content.
        return Frame(Packet(header, payload),bytes[1]);
        


#test code for Frame
if(__name__ == '__main__'):
    restartBytes = [1,2,12,4,5,6,7,8,9,10,11,182,13,15,28];  #Test byte sequence for Restart packet for proof testing purposes.
    
    pointReplyBytes = [1,1,53,228,0,0,253,18,0,4,0,149,0,0,0,12,1,0,1,0,1,197,129,0,2,0,1, # Real Test byte sequence for Point Info packet reply for proof testing purposes.
                      254,1,0,126,65,0,0,0,0,0,0,3,1,9,0,42,0,0,4,0,4,0,4,0,0,0,0,0,27];

    ResultFrame = LocalFrameFormatter().format(pointReplyBytes);

    print (ResultFrame.getByteArray());