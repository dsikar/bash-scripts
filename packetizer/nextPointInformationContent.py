from content import Content;

class NextPointInformationContent(Content):
    """Class to populate content for point information packet"""
    def __init__(self, **kwargs):

          attributes  =  {
               'clientID'  : 0x0000, #Double bytes
              };

          for key in kwargs:
              if ((key in attributes) != True):
                raise ValueError(key);
              attributes[key]=  kwargs[key];
          Content.__init__(self, **attributes);

    def getByteArray(self):

        bytes  = Content.createSizeArray(2, 0x00);
        bytes[0] = self.getLSB(self.getParameter('clientID'));
        bytes[1] = self.getMSB(self.getParameter('clientID'));

        return bytes;
