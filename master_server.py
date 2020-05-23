MasterMaster
import atexit as exit
import select
import tkinter
import atexit
import time
import threading
import socket as socket
import socketserver as socketserver
import sys


class MasterServer:
    BUF_LEN = 4096
    address_family = tuple((socket.AF_INET, socket.SOCK_STREAM))
    socket = None
    bindingData = None
    controlThread = None
    newConnectionsThread = None

    def __init__(self, port, listenFor=3):
        self.bindingData = (socket.gethostbyname(
            socket.gethostname()), int(port))
        self.robotsToListenFor = listenFor

    def start_server(self):
        atexit.register(self.onExit)
        self.controlThread = threading.Thread(group=None, target=self.doTasks)
        self.newConnectionThread = threading.Thread(
            group=None, target=self.acceptConnections)

        try:
            self.socket = socket.socket(self.address_family)
            self.socket.bind(self.bindingData)
            self.socket.listen(self.robotsToListenFor)
        except socket.error as socketError:
            print(socketError)
            quit(-1)
        except socket.gaierror as gaiError:
            print(gaiError)
            quit(-1)
        except socket.timeout as timeError:
            print(timeError)
            quit(-1)

        self.newConnectionThread.run()
        self.controlThread.run()

    def acceptConnections(self):
        while(True):    #TODO: Implement authentication/encryption here.
            connection, host = self.socket.accept()
            print("Got connection from: ", host)
    def doTasks(self):
        try:
            pass         #TODO: Implement control logic
        except socket.error as socketError:
            print(socketError)
            quit(-1)
        except socket.gaierror as gaiError:
            print(gaiError)
            quit(-1)
        except socket.timeout as timeError:
            print(timeError)
            quit(-1)

    def onExit(self):
        pass

if __name__ == '__main__' and len(sys.argv) ==2:
    MasterServer(int(sys.argv[1]),  3)
else:
    print("To use:\tpython\t.\master_server.py\t<port-num>")