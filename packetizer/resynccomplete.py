from content import Content;


class ResyncComplete(Content):

    def __init__(self, **kwargs):
        params   = {
            "resynchronisationData"     : 0x00,
            "avaliable"                 : 0x00,
            "resynchronisationSent"     : 0x00
         };
        
        for key in  kwargs:
            if  key in params:
                params[key]  =  kwargs[key];

        Content.__init__(self,**params) ;

    
    def getByteArray(self):
        data    = self.createSizeArray(4, 0x00);
        data[0] = self.getParameter("resynchronisationData");
        data[1] = self.getParameter("avaliable");
        data[2] = self.getParameter("resynchronisationSent");
        return data;
