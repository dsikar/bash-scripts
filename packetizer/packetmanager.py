from registry import PacketRegistry;
from header import LOCAL_HEADER, NETWORK_HEADER; 
from frame  import Frame;
from logon import LogonContent;
from restartcontent import RestartContent;
import packet ;
import packetids as id;
from loopcontrolrequest import LoopControlRequest


class PacketManager:
    __registry = None;

    @staticmethod
    def registerContentType(type, content):
        if(PacketManager.__registry == None):
            PacketManager.__registry = PacketRegistry.getInstance();
        PacketManager.__registry.register(type, content);

    @staticmethod 
    def createPacket(packettype, headerType = LOCAL_HEADER):
        packettype  =  packettype if(type(packettype) == int)  else  None;
        if(packettype  == None):
            raise AttributeError("@createFrame: packet id must not be a None value");
        return PacketRegistry.createPacket(packettype,headerType);

    @staticmethod
    def initialize():
        PacketManager.registerContentType(id.spkd_ID_RESTART_REQUEST , RestartContent);
        PacketManager.registerContentType(id.spkd_ID_NGUI_CLIENT_SERVICE_SUPPORT, LogonContent);
        PacketManager.registerContentType(id.spkd_ID_LOOP_SHUTDOWN_RESTART, LoopControlRequest);
        


