from IDataFormatter import IDataFormatter;
from loopcontrolrequest import LoopControlRequest;
""" ****************************************************************************
*@brief
*  The class is provided for parsing the bytes for LoopControlRequest
*  Input: the Body bytes which is LoopControlRequest bytes
*  Output: the LoopControlRequest Body
**************************************************************************** """
class LoopControlRequestFormatter(IDataFormatter):
    def format(self, bytes):
        Body = None;
        if(len(bytes) != 2):
            raise ValueError("@LoopControlRequestFormatter: LoopControlRequestFormatter require two bytes")
        else:
            Body = LoopControlRequest(controlID=bytes[0],loopID=bytes[1]);
        return Body;
# test code for Body
if(__name__ == '__main__'):
    bytes = [0,20];
    body = LoopControlRequestFormatter().format(bytes);
    print(body.getByteArray())
