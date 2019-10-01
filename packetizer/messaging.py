"""***************************************************
* @brief
*  A simple message pattern that can be possibly use to communication btw 
* Comports or between objects  
***************************************************"""

class Event:
    def __init__(self, type, playload):
        self.__playload         =  playload;
        self.__stopPropagation   = False;
        self.__type = type;

    @property
    def stopPropagation(self):
        return self.__stopPropagation;

    @stopPropagation.setter
    def stopPropagation(self, value):
        self.__stopPropagation  = value;

    @property
    def playload(self):
        return self.__playload;

    @property
    def type(self):
       return self.__type;
"""******************************************************************
*
  Subscriber
******************************************************************"""
class Subscriber:
    def onEvent(self,sender , event):
         raise  NotImplementedError("Observer: @onEvent");

"""************************************************************************
* @brief
*  Publisher base class.
************************************************************************"""
class Publisher:
    def __init__(self):
        self.__subscribers     =  [];  
        self.__stopPropagation = False;

    #Send the event to all the listeners.
    def publish(self, event):
        self.__stopPropagation = False;
        for sub in  self.__subscribers:
            if( (sub != None) and (isinstance(sub, Subscriber))):
                if(self.__stopPropagation != True):
                    sub.onEvent(self, event);
                else:
                    break;
    @property
    def stopPropagation(self):
        self.__stopPropagation = True;

    def subscribe(self, observer):
        if(self.__exists(observer) != True):
            self.__subscribers.append(observer);

    def unsubscribe(self , observer):
        if(self.__exists(observer)):
            self.__subscribers.remove(observer);
            pass;

    def __exists(self, observer):
        found  = False;
        if(observer != None):
            for obser in self.__subscribers:
                if(obser ==  observer):
                    found  = True;
                    break;
        return found;


class PortListener(Subscriber):

    def onEvent(self, sender, event):
         print(event);
         pass;

#Simple test
if(__name__ == '__main__'):
    publisher  = Publisher();
    publisher.subscribe(PortListener());
    publisher.subscribe(PortListener());
    publisher.publish({"name" : 'Obaro'});