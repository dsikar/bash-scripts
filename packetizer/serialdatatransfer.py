import serial;
from IDataTransfer import IDataTransfer, ITimableObject;
""" ****************************************************************************
*@brief
*  The abstract class provides SerialDataTransfer object 
*  to support data transfer over COM serial interfaces
**************************************************************************** """

# default settings
BAUDRATE = 115200;
TIMEOUT  = 3;

class SerialDataTransfer(IDataTransfer,ITimableObject):

  def __init__(self, serial_port, baudrate  = BAUDRATE, timeout  =  TIMEOUT  ):
    self.__serial =  self.__initialDefaultSettings(serial_port, baudrate,timeout  )

  def Write(self, data):
    return self.__serial.write(data)
  def Read(self):
    return self.__serial.read();
 
  def GetTimeout(self):
    return self.__serial.timeout;

  def SetTimeout(self, value):
    if(self.__serial != None):
      if hasattr(self.__serial, 'cancel_read'):
        self.__serial.timeout = value; 

  def CancelRead(self):
    if hasattr(self.__serial, 'cancel_read'):
      self.__serial.cancel_read();
  
  def IsDataAvailable(self):
    status  = False;
    if(isinstance(self.__serial, serial.Serial)):
      status =  (self.__serial.in_waiting > 0);
    return status;

  def IsConnected(self):
    result  = False;
    if(isinstance(self.__serial, serial.Serial)):
      result  = self.__serial.is_open;
    return result;

  def CanRead(self):
    result  = False;
    if(isinstance(self.__serial, serial.Serial)):
      result = (self.__serial._checkReadable != 0);
    return result;

  def CanWrite(self):
    result  = False;
    if(isinstance(self.__serial, serial.Serial)):
      result = (self.__serial._checkWritable != 0);
    return result;

  def Close(self):
    if(isinstance(self.__serial, serial.Serial)):
        if(self.__serial.is_open):
            self.__serial.close()

  def __initialDefaultSettings(self,portName,baudrate,timeout):
    try:
        serial_obj 	= serial.Serial(
                                    port 		= portName,
                                    baudrate 	= baudrate,
                                    timeout		= timeout,
                                    bytesize 	= serial.EIGHTBITS,
                                    parity 		= serial.PARITY_NONE,
                                    stopbits 	= serial.STOPBITS_ONE);
    except IOError:
        print "The specified serial port cannot be open."
        return False
    else:
        return serial_obj


#simple test code
if(__name__=='__main__'):
    COMPORT = "COM1"
    print "opening new interface on com: " + COMPORT
    test = SerialDataTransfer(COMPORT)
    if (test.isConnected()):
        print "isConnected: " + str(test.IsConnected())
        print "CanRead: " + str(test.CanRead())
        print "CanWrite: " + str(test.CanWrite())
        print "isDataAvailable: " + str(test.IsDataAvailable())
        print "getTimeout: " + str(test.GetTimeout())
        print "setTimeout to 5"
        test.setTimeout(5)
        print "getTimeout: " + str(test.GetTimeout())
        print "interface closed"
        test.close()
        print "isConnected: " + str(test.IsConnected())