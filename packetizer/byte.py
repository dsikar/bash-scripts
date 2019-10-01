"""****************************************************************
* @brief
*  The class is use to manipulate bits
*  This can be use 
****************************************************************"""

import struct;
BYTE_LENGTH  = 0x08;

class Byte:

  def __init__(self, value):
      self.__value  = Byte.getByte(value);

  def __add__(self, other):
     value  =   self.__getByte(other);
     self.__value =  value  | self.__value;
     return self;

  def __sub__(self, other):
    return self.__add__(other * -1);

  #This make sure that the value return is always 8bits
  @staticmethod
  def getByte(value):
      result =  0;
      if(value != None):
          intVal =  int(value);
          bytes  =  struct.pack('i', intVal);
          if(len(bytes) > 0):
            result =  ord(bytes[0]);
      return  result;

  def __ne__(self, other):
    return self.__value != Byte.getByte(other);

  #Get a binary value
  def to_string(self, leading  = BYTE_LENGTH):
      return "{0:b}".format(self.__value).zfill(leading);

  def get_value(self):
      return self.__value;

  def is_set(self, pos):
     if(pos < 0 and pos >= BYTE_LENGTH ):
       raise AttributeError("@Expecting an integer value");
     bits = list(reversed(self.to_string()));
     return (int(bits[pos]) == 1);

  #Set the bit values
  def set(self , pos):
    if(pos >= 0 and pos < BYTE_LENGTH ):
      self.__value   = (self.__value | (1 << pos));
    else:
      raise ValueError("@pos must be an integer and at range(0,7)");

  def clear(self, pos):
    if(pos >= 0 and pos < BYTE_LENGTH ):
      self.__value   = (self.__value &  ~(1 << pos));
    else:
      raise ValueError("@pos must be an integer and at range(0,7)");

  def toggle(self, pos):
    if(pos >= 0 and pos < BYTE_LENGTH ):
       self.__value   = (self.__value ^  (1 << pos));
    else:
      raise ValueError("@pos must be an integer and at range(0,7)");

  def test(self, pos):
     result  = 0;
     if(pos >= 0 and pos < BYTE_LENGTH ):
       result   = (self.__value &  (1 << pos));
     else:
      raise ValueError("@pos must be an integer and at range(0,7)");
     return  result;

  """
   Get a byte range and construct another a byte with it.
  """
  def get_byte_from(self, startbit, endbit):
     result  = "";
     values =  list(reversed(self.to_string()));
     for index in range(startbit,endbit + 1):
       result+=  values[index];
     result = ''.join(reversed(result));
     return Byte(int(result, 2));

  @property
  def length(self):
     return length(self.to_string());

  #Return the value.
  def __str__(self):
    return hex(self.__value);


if(__name__ == "__main__"):
  byte  = Byte(100);
  print(byte.to_string());
  byte.set(0);
  print(byte.to_string())
  byte.clear(4);
  if(byte.is_set(4)):
    print("Bit 4th is set");
  print(byte.to_string())
  print(byte.get_byte_from(2,4));
