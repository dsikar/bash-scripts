import threading;
from byte import Byte;
import Queue;
import time;


class ByteBuffer(Queue.Queue):

    def __init__(self):
       Queue.Queue.__init__(self);
   
    def peek(self , intPos = 0):       
        val = None;
        if((intPos >= 0)  and (intPos < self.qsize())):
             val  = self.queue[intPos]
        return val;

   
    def __str__(self):
        result  = "";
        for a in self.queue:
            result += a + ',';
        del result[:-1];
        return result;

buffer = None;    
stop  = False;
def putter():
    for i in range(0, 100):
       time.sleep(10);
       buffer.put(i);
    stop = True;




if(__name__=='__main__'):
    buffer  =  ByteBuffer();
    t1 = threading.Thread(target=putter);
    t1.start();
    while(stop != True):
      c = buffer.peek(0);
      print('peek  = {0}'.format(c));
      c = buffer.get();
      print(c);
 