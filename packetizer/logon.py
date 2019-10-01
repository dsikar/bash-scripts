
from content import Content;

USER_LOG_ON_VALIDATION     = 0x02;
CURRENT_USER_LOG_OFF       = 0x03;
LOGGED_ON_USER_INFORMATION = 0x04;
HIGH_PRIORITY_STTAUS_COUNT = 0x05;

class LogonContent(Content):

    def __init__(self,**kwargs):

        params  =  {
               'serviceID'     : 0x02,
               'userID'        : 0x00,
               'encodingType'  : 0x00,
               'length'        : 0x00,
               "userAccessLevel"  : 0x00,
               "userID"         : 0x00,
               "userNameLength" : 0x00,
               "userName"       : "",
               "systemStatus"        : 0x00,
               "systemStatusExtended": 0x00,
               "numberOfCounters"     :0x00,
               "counters"            : {}, # {'key' = counterID , counter'}
               "currentNetMaster"    : 0x00,
               'passcode'            : "000000",
            };

        for key in kwargs:
            if(key in params) != True:
                raise ValueError("@LogonContent : invalid parameter {0} ".format(key));
            else:
                params[key]  = kwargs[key];

        if(isinstance(params['passcode'], basestring)) != True:
           raise ValueError("@LogonContent: expecting passcode to be a string object.");
        Content.__init__(self,**params); 

    def validate(self, key, value):
        valid  =  Content.validate(self, key, value);
        if(valid != True):
            if(key == 'counters'):
                 valid = True;
        return valid;

    def setParameter(self, stype, values):
        if(stype =='counters'):
            if(self.validate(stype, values)):
                if(type(values)  == dict):
                    counter  =  self.getParameter(stype);
                    for key in values:
                       counter[key]  = values[key];
                    self._params[stype] =  counter;
        else:
            Content.setParameter(self, stype, values)

    def getByteArray(self):
        serviceID  = self.getParameter("serviceID");
        bytes      =  None;

        if(serviceID == USER_LOG_ON_VALIDATION):
           passwordBytes  = self.getParameter("passcode");
           bytes          = self.createSizeArray(4, 0x00);
           self.setParameter("length", len(passwordBytes));

           bytes[0]  =  serviceID;
           bytes[1]  =  self.getParameter("userID");
           bytes[2]  =  self.getParameter("encodingType");
           bytes[3]  =  self.getParameter("length");

           for char  in passwordBytes:
               bytes.append(ord(char));
        elif (CURRENT_USER_LOG_OFF == serviceID):
         bytes     =  self.createSizeArray(1, 0x03);
         bytes[0]  =  serviceID;

        elif(LOGGED_ON_USER_INFORMATION == serviceID):
            bytes          = self.createSizeArray(4, 0x00);
            bytes[0]       = serviceID;
            bytes[1]       = self.getParameter("userID");
            bytes[2]       = self.getParameter("userAccessLevel");
            userName       = self.getParameter("userName");
            self.setParameter("userNameLength" , len(userName));
            bytes[3]       = self.getParameter("userNameLength");
            for char  in userName:
               bytes.append(ord(char));
        elif(HIGH_PRIORITY_STTAUS_COUNT  == serviceID):
            bytes          = self.createSizeArray(5, 0x00);
            bytes[0]                    = serviceID;
            bytes[1]         = self.getParameter("systemStatus");
            #System extended is 16bytes and need to be split.
            byte16           = self.getParameter("systemStatusExtended");
            bytes[2]         = self.getMSB(byte16);
            bytes[3]         = self.getLSB(byte16);
            counters         = self.getParameter("counters");
            self.setParameter("numberOfCounters", len(counters));
            bytes[4]         = self.getParameter("numberOfCounters");
            for attr in counters:
                bytes.append(attr);
                byte16  = counters[attr];
                #Counter is 16byte and need to be split.
                bytes.append(self.getMSB(byte16));
                bytes.append(self.getLSB(byte16));
            bytes.append(self.getParameter("currentNetMaster"));

        return bytes;


