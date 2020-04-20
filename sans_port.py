#sans ports
#pip install termcolor
#pip install sockets
#pip install DateTime
#pip install threaded
 
import socket
import os
import threading
from datetime import datetime
from termcolor import colored

 
def ports():
    os.system('clear')

    lresult = "==========================="
 
    print(colored('''
                             VERSION:1.0.0
 --------------------------------------------------------------------------
|                                                                          |
|  _$$$$____$$$$___$$__$$___$$$$___$$$$$____$$$$___$$$$$___$$$$$$___$$$$   |
|  $$______$$__$$__$$$_$$__$$______$$__$$__$$__$$__$$__$$____$$____$$      |
|  _$$$$___$$$$$$__$$_$$$___$$$$___$$$$$___$$__$$__$$$$$_____$$_____$$$$   |
|  ____$$__$$__$$__$$__$$______$$__$$______$$__$$__$$__$$____$$________$$  |
|  _$$$$___$$__$$__$$__$$___$$$$___$$_______$$$$___$$__$$____$$_____$$$$   |
|                                                                          |
 --------------------------------------------------------------------------
''', 'green'))
 
    print(colored('>>>without http and https example www.youtube.com!!! \n','red'))
 
    #soket
    ip = input(colored('Enter_link:>>> ','yellow'))
    print()
    def scan_port(ip,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            connect = sock.connect((ip,port))
            print(lresult)
            print(colored('[ PORT: >>>','yellow'),port,colored('<<< :OPEN ] ','green'))
            print(lresult,'\n')
            connect.close()
        except:
            pass
    for i in range(1000):
        potoc = threading.Thread(target=scan_port, args=(ip,i))
        potoc.start()
#==============================
#time result port
    start = datetime.now()
    ends = datetime.now()
    print('Time : {}'.format(ends-start))
#===============================

ports()

while True:
    Enter = input(colored('\nPress Enter','yellow'))
    os.system('clear')
    ports()