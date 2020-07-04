import phonenumbers
from phonenumbers import carrier
import socket
import random
from bs4 import BeautifulSoup
import requests
import pyshorteners
import time
import sys
print("""
##########################
#        OXHACK          #
#      Azerbaijan        #
#                        #
#        Amateur Hacker  #
##########################
""")

print(""" 1) Telefon nömresi operatoru tapma
2) Güclü şifre yaratma 
3) Instagram haqqinda melumat

-----------------------------
00) Cixis""")

while True:
    prosses=int(input("Prossesi daxil edin :  "))


    if prosses==1:
        haqq= int(input("Neçə nömre axtaracaqsınız :"))
        i=0
        while i<haqq :
            i= i+1
            mobileNo = input("Telefon nomresini daxil edin : ")

            service_provider = phonenumbers.parse(mobileNo)
            print (carrier.name_for_number(service_provider ,"en" ))

    elif prosses==2:
        simvollar = "qwertyuiopasdfghjklzxcvbnm1234567890&@"
        while True:

            sifre_uzunlugu = int(input("Şifre neçe simvoldan ibaret olsun :  "))
            sifre ="".join(random.sample(simvollar,sifre_uzunlugu))
            print(sifre)

    elif prosses==3:
        url = input("Enter url --> ")
        print ("URL after shortining --> " , pyshorteners.Shortener().tinyurl.short(url))
    
    elif prosses==00:
        print ("Cixis edilir . . . ")
        time.sleep(3)
        sys.exit()