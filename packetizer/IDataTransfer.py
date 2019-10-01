""" ****************************************************************************
*@brief
*  The abstract class provides IDataTransfer object 
*  to support data transfer on multiple interfaces
**************************************************************************** """
class IDataTransfer:
    def IsDataAvailable(self):
        raise NotImplementedError("@isDataAvailable: the method is not implemented.");
    def IsConnected(self):
        raise NotImplementedError("@isConnected: the method is not implemented.");
    def Write(self, data):
        raise NotImplementedError("@Write: the method is not implemented.");
    def Read(self):
        raise NotImplementedError("@Read: the method is not implemented.");
    def CanRead(self):
        raise NotImplementedError("@CanRead: the method is not implemented.");
    def CanWrite(self):
        raise NotImplementedError("@CanWrite: the method is not implemented.");

"""************************************
*************************************"""
class ICancellable:
   def CanCancel(self):
        raise NotImplementedError("@canCancel: the method is not implemented.");
class ICancellable:
   def  Cancel(self):
         raise NotImplementedError("@Cancel: the method is not implemented.");



class ITimableObject:
    def SetTimeout(self, value):
          raise NotImplementedError("@setTimeout: the method is not implemented.");
    def GetTimeout(self):
          raise NotImplementedError("@getTimeout: the method is not implemented.");