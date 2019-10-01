
from content import Content;

class RestartContent(Content):

    def __init__(self, **kwargs):
        if(len(kwargs) > 1):
            raise TypeError("@Restart Content require only 1 parameter");
        if("restartOption" in kwargs) != True:
            kwargs['restartOption'] = 0;
        Content.__init__(self,  **kwargs);

    def validate(self, key , value):
        valid  = False;
        if(key  == "restartOption"):
            valid = True;
        return valid;

    def getByteArray(self):
        expectedFields = {"restartOption" : 0}
        bytes  = Content.getByteArray(self);
        if(len(bytes) <= 1):
            if(len(bytes) < 1):
                bytes.append(0);
        else:
            raise AssertionError("@RestartContent:restart-option expected.");
        return bytes;

