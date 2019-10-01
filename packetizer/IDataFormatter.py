""" ****************************************************************************
*@brief
*  The abstract class provided IDataFormatter interface 
*  for taking a string of bytes and parse it into a packet.
**************************************************************************** """
class IDataFormatter:
    def format(self , bytes):
        raise NotImplementError("@IDataFormatter format function needs to be implemented.");
    
    def _combineBytes(self, msByte, lsByte):
        raise NotImplementedError("@IDataFormatter combineBytes function need to be implemented by subclass");