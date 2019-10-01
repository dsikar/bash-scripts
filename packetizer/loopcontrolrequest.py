from content import Content

#spkd_ID_LOOP_SHUTDOWN_RESTART
PACKET_LEN = 2 #bytes

class LoopControlRequest(Content):

  def __init__(self, **kwargs):
    if(len(kwargs) > PACKET_LEN):
      raise TypeError("@Packet parameter content was exceeded.")
    params   = {
                  "controlID"     : 0x00, #0-2
                  "loopID"        : 0x01, #1-32
    }
        
    for key in  kwargs:
       if  key in params:
          params[key]  =  kwargs[key];
       else:
         raise ValueError("@LoopContentRequest: Invalid parameter {0}  found".format(key));

    Content.__init__(self,**params) 

    
    def getByteArray(self):
        data    = self.createSizeArray(PACKET_LEN, 0x00)
        data[0] = self.getParameter("controlID")
        data[1] = self.getParameter("loopID")
        return data

if(__name__ == '__main__'):
  content  =  LoopControlRequest(controlID = 2 );
  print(content.getByteArray());