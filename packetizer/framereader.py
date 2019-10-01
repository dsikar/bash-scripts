from readers import DataReader, BadPacketReadError , IStartableObject;
from serialdatatransfer import SerialDataTransfer;
from packet import Packet;
from restartcontent import RestartContent;
from header import LocalHeader;
import packetids as ids;
from frame import Frame,ACK;
from byte import Byte;
from messaging import  Publisher,Event;
from LocalFrameFormatter import LocalFrameFormatter;
import threading;
INVALID_FRAME_ERROR  = 0x04;

class IFrameReader(IStartableObject):
     def Next(self):
        raise NotImplementedError("@DataReader: read the data object.");
  
class PTPFrameReader(Publisher , IFrameReader):
      def __init__(self , port, **kwargs):
          self.__dataReader  =  (kwargs['dataReader'])  if ('dataReader' in kwargs) else DataReader(SerialDataTransfer(port));
          self.__mutex  =  threading.Lock();
      def Start(self):
          if(self.__dataReader != None):
              self.__dataReader.Start();
         
      """******************************************************************
      *@brief
      *  The function should able to return a frame object from recieved mx frame.
      ******************************************************************"""
      def Next(self):
        with self.__mutex:
            frame  =  None;
            try:
                bytes =  self.__dataReader.Read();
                if( (bytes != None) and (len(bytes) > 0)):
                    #create a valid frame object if possible other throw an exception.
                    try:
                      if(len(bytes) > 1):
                         formatter  =  LocalFrameFormatter();
                         frame = formatter.format(bytes);
                    except Exception as frameError:
                        raise BadPacketReadError(frameError.message,bytes, INVALID_FRAME_ERROR );
                
            except Exception as err:
                print err;
            return frame;
"""
When the Panel is restart , a default packet is send via the consys port.
with packet ID  = 78
   # 01 00 12 00 00 00 00 00 00 00  00 00 182 00 01
"""
if(__name__ == '__main__'):
    restart      = Packet(LocalHeader(ids.spkd_ID_RESTART_REQUEST), RestartContent());
    frameObject  =  Frame(restart,0);
    reader       =  PTPFrameReader("COM8");
    reader.Start();
    while(reader != None):
       frame  =  reader.Next();
       if(frame != None):
          event  = Event(01, frame);
          reader.publish(event);
     