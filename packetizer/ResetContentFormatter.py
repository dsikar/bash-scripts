from IDataFormatter import IDataFormatter;
from restartcontent import RestartContent;
""" ****************************************************************************
*@brief
*  The class is provided for parsing the bytes for ResetContent
*  Input: the Body bytes which is ResetContent bytes
*  Output: the Reset Body
**************************************************************************** """
class ResetContentFormatter(IDataFormatter):
    def format(self, bytes):
        Body = None;
        if(len(bytes) != 1):
            raise ValueError("@ResetContentFormatter: Reset formatter require just one bytes")
        else:
            Body = RestartContent(restartOption=bytes[0]);
        return Body;
# test code for Body
if(__name__ == '__main__'):
    bytes = [76];
    body = ResetContentFormatter().format(bytes);
    print(body.getByteArray())

