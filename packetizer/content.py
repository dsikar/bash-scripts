""" ****************************************************************************
*@brief
*  The class content contain the content of the playload.
*  its wrapper in class so that users can verify and validated packet before its send.
**************************************************************************** """

"""
The abstract class provided interface to convert a serial of list into
a data array.
"""

import struct;




class ByteContainer:

    def getByteArray(self):
        raise NotImplementError("@getDataArray need to be implemented.");

    def setParameter(self, stype , value):
        raise NotImplementError("@setParameter need to be implemented.");

    def getParameter(self, stype):
        raise NotImplementError("@getParameter need to be implemented.");

    def count(self):
        raise NotImplementError("@count need to be implemented.");

    @staticmethod
    def createSizeArray(size , defaultValue):
        lst  = list();
        for index   in range(0, size):
            lst.append(defaultValue);
        return lst;

    @staticmethod
    def getMSB(x):
        byte =  x;
        if(type(x) != int):
            byte  =  ord(x);
        bytes  =  struct.pack('i', byte);
        return ord(bytes[0]);

    @staticmethod
    def getLSB(x):
        result =  0x00;
        byte =  x;
        if(type(x) != int):
            byte  =  ord(x);
        bytes  =  struct.pack('i', byte);
        if(len(bytes) > 1):
            result  =  bytes[1];
        return ord(result);




class ValueValidator:
    def validate(self , key , value):
      raise NotImplementedError("@ValueValidator::validate must be implemented.");


class Content(ByteContainer,  ValueValidator):

    def __init__(self, **kwargs):
      self._params  =  dict();
      for attr  in kwargs:
          self._params[attr] = kwargs[attr];

    def setParameter(self, stype , value):
        if(self.validate(stype , value)):
            self._params[stype] = value;
        else:
            raise AttributeError("Invalid packet content parameter ("+stype+")");

        return self;

    def getParameter(self, stype):
         result = None;
         if stype in self._params:
             result =  self._params[stype];
         return result;

    """
    @description
      The function should be override in every content type that need to be defined.
      @return {List: object} a list of bytes.
    """
    def getByteArray(self):
        data  =  list();
        for  attr in self._params:
            data.append(self._params[attr]);
        return data;

    def validate(self, key , value):
        valid =  False;
        if( key in self._params ):
            valid = True;
        return valid;

    def count(self):
        return len(self._params);

    @property
    def size(self):
        return self.count();