import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import random
import pyshorteners
import time
import sys
import platform
import socket
from socket import * 
from colorama import Fore , Back


print( Fore.RED +"""
#####################################################
#                                                   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#               OxHack 1.0 V                        #
#       https://github.com/nizambaxisov/            #
#                                                   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                                   #
#####################################################
""")

print("""1) Telefon nömresi ölke ve operator 
2) Güclü şifre yaratma 
3) Link qısaltma
4) Cihaz haqqında melumat
5) Sayt IP adress tapma
6) Port Skanner 

 / ------------------------------/
/-------------------------------/ 

00) Cixis""")

while True:
    prosses=int(input("Prossesi daxil edin :  "))


    if prosses==1:
        haqq= int(input("Neçə nömre axtaracaqsınız :"))
        i=0
        while i<haqq :
            i= i+1
            number = input("Telefon nömresini daxil edin  : ")
            ch_number = phonenumbers.parse(number , 'CH')
            print (geocoder.description_for_number(ch_number , "az"))
            s_num = phonenumbers.parse(number , 'RO')
            print (carrier.name_for_number(s_num , "en"))
    elif prosses==2:
        simvollar = "qwertyuiopasdfghjklzxcvbnm1234567890&@"
        while True:

            sifre_uzunlugu = int(input("Şifre neçe simvoldan ibaret olsun :  "))
            sifre ="".join(random.sample(simvollar,sifre_uzunlugu))
            print(sifre)

    elif prosses==3:
        url = input("Enter url --> ")
        print ("URL after shortining --> " , pyshorteners.Shortener().tinyurl.short(url))
    
    elif prosses==4:
        print ("Emeliyyat sisteminiz " + platform.system())
        print ("Prosessorunuz " + platform.processor())
        print ("Platformunuz " + platform.platform())
  
    elif prosses==5:
        sayt = input("IP adressi tapılacaq saytı daxil edin : ")
        ip_adress = gethostbyname(sayt)
        print (sayt+ "'ın ip adressi --->  "+ Fore.GREEN + ip_adress)

    elif prosses==6:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        host = input("IP adress : ")

        def portscanner(port):
            if s.connect_ex((host , port)):
                print("Port %d is closed"%port)
            else:
                print("Port %d is open "%port)

        for port in range(1,1000):
            portscanner(port)
    
    
    elif prosses==00:
        print ("Cixis edilir . . . ")
        time.sleep(3)
        sys.exit() 
    
