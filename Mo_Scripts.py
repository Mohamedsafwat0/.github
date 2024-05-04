import requests
import os
import requests
import random
import pyfiglet
import string
from getuseragent import UserAgent
import webbrowser
import time
from time import sleep
import sys
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح.
C = "\033[1;97m"  # ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
#Color
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
m500 = 'https://raw.githubusercontent.com/Mohamedsafwat0/.github/main/500Mg.py'
spam = 'https://raw.githubusercontent.com/Mohamedsafwat0/.github/main/Spam_Whatsapp.py'
spam2 = 'https://raw.githubusercontent.com/Mohamedsafwat0/.github/main/SpamforAll.py'
Etislat = 'https://raw.githubusercontent.com/Mohamedsafwat0/.github/main/2H_etisalat.py'

def main():
    clear_screen()
    


print(X+"----------------------  Welcome My Scripts -----------------")
time.sleep(1.5)
print()
print(B+"="*60)
time.sleep(1.5)
Print("""
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
print(A+"""
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
print(Z+"""
[1] 500 Mg Orange

[2] spam WhatsApp 

[3] spam sms all Network 

[4] Two hours Etisalat of free social  
 
""")
number = int(input(F+"Choose The Scripts Pro: \033[1;33m"))
clear_screen()  # مسح الشاشة بعد اختيار المستخدم لرقم
if number == 1:
        Mo = m500
elif number == 2:
        Mo = spam
elif number == 3:
        Mo = spam2
elif number == 4:
        Mo = Etislat

else:
        print("Wrong choice❌❌")
        
         

try:
        response = requests.get(Mo)
        response.raise_for_status()
        junku = response.text
        exec(junku)
except requests.exceptions.RequestException as e:
        print("Error❌❌")

if __name__ == "__main__":
    main()
