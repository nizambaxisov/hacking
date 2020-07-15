import os
import time
import sys
cavab = input("Tool üçün lazım olan modulların yüklənməsini təstiqləyirsiniz [beli] yoxsa [xeyr] : ").lower
if cavab =="beli" or cavab=="b":
    print("Prosses başlanır . . . ")
    time.sleep(2)
    os.system("pip install phonenumbers")
    os.system("pip install pyshorteners")
    os.system("pip install socket")
    os.system("pip install colorama")


