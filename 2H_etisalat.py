import requests
import base64
import xml.etree.ElementTree as ET
from colorama import Fore
from pyfiglet import Figlet
import webbrowser
import requests, os, sys, time, pyfiglet
from time import sleep
Hamo1 = '\033[1;31m'  # احمر
Hamo2 = '\033[1;33m'  # اصفر
Hamo3 = '\033[2;32m'  # اخضر
Hamo4 = "\033[1;97m"  # ابيض
Hamo5 = '\033[2;36m'  # سمائي
Hamo6 = '\033[1;34m'  # ازرق فاتح.
Hamo7 = "\033[1;97m"  # ابيض
Hamo8 = '\033[1;31m'
Hamo9 = '\033[2;36m'
Hamo10 = '\033[1;32m'
Hamo11 = '\033[1;33m'

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
print(F+"-------- Welcome My Script {Two hours social Etisalat } ----")
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
Hamo12 = input(Hamo1 + "Enter Your Email : " + Hamo2)
time.sleep(1.5)
print()
Hamo13 = input(Hamo1 + "Enter Your Password : " + Hamo2)
time.sleep(1.5)
print()
Hamo14 = input(Hamo1 + "Enter Your Number : " + Hamo2)
time.sleep(1.5)
print()
m=int(input(Hamo1 +"Entar a Repeat : " + Hamo2))
for _ in range(m):

    if "01" in Hamo14:
        Hamo15 = Hamo14[+1:]
    else:
        Hamo15 = Hamo14

    Hamo16 = Hamo12 + ":" + Hamo13
    Hamo17 = Hamo16.encode("ascii")
    Hamo18 = base64.b64encode(Hamo17)
    Hamo19 = Hamo18.decode("ascii")
    Hamo20 = "Basic" + " " + Hamo19

    Hamo21 = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"

    Hamo22 = {
        "applicationVersion": "2",
        "applicationName": "MAB",
        "Accept": "text/xml",
        "Authorization": Hamo20,
        "APP-BuildNumber": "964",
        "APP-Version": "27.0.0",
        "OS-Type": "Android",
        "OS-Version": "12",
        "APP-STORE": "GOOGLE",
        "Is-Corporate": "false",
        "Content-Type": "text/xml; charset=UTF-8",
        "Content-Length": "1375",
        "Host": "mab.etisalat.com.eg:11003",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/5.0.0-alpha.11",
        "ADRUM_1": "isMobile:true",
        "ADRUM": "isAjax:true"
        
    }

    Hamo23 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
    Hamo24 = requests.post(Hamo21, headers=Hamo22, data=Hamo23)

    if "true" in Hamo24.text:
        st = Hamo24.headers["Set-Cookie"]
        ck = st.split(";")[0]
        br = Hamo24.headers["auth"]

        Hamo25 = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/offersV3?req=<dialAndLanguageRequest><subscriberNumber>%s</subscriberNumber><language>1</language></dialAndLanguageRequest>" % (Hamo15)

        Hamo26 = {
            'applicationVersion': "2",
            'Content-Type': "text/xml",
            'applicationName': "MAB",
            'Accept': "text/xml",
            'Language': "ar",
            'APP-BuildNumber': "10459",
            'APP-Version': "29.9.0",
            'OS-Type': "Android",
            'OS-Version': "11",
            'APP-STORE': "GOOGLE",
            'auth': "Bearer " + br,
            'Host': "mab.etisalat.com.eg:11003",
            'Is-Corporate': "false",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'User-Agent': "okhttp/5.0.0-alpha.11",
            'Cookie': ck
        }

        Hamo27 = requests.get(Hamo25, headers=Hamo26)

        if Hamo27.status_code == 200:
            root = ET.fromstring(Hamo27.text)
            Hamo28 = None
            for category in root.findall('.//mabCategory'):
                for product in category.findall('.//mabProduct'):
                    for parameter in product.findall('.//fulfilmentParameter'):
                        if parameter.find('name').text == 'Offer_ID':
                            Hamo28 = parameter.find('value').text
                            break
                    if Hamo28:
                        break
                if Hamo28:
                    break
        else:
            print(Hamo6 + "هذا العرض غير متاح ، حاول بكره ")

    else:
        print(Hamo1 + "الحساب غير صحيح")

    if "true" in Hamo24.text:
        st = Hamo24.headers["Set-Cookie"]
        ck = st.split(";")[0]
        br = Hamo24.headers["auth"]

        Hamo29 = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/submitOrder"

        Hamo30 = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Cookie": ck,
            "Language": "ar",
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "auth": "Bearer " + br + "",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "User-Agent": "okhttp/5.0.0-alpha.11"
        }

        Hamo31 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><parameters><parameter><name>GIFT_FULLFILMENT_PARAMETERS</name><value>Offer_ID:%s;ACTIVATE:True;isRTIM:Y</value></parameter></parameters><productName>FAN_ZONE_HOURLY_BUNDLE</productName></submitOrderRequest>" % (
        Hamo15, Hamo28)

        Hamo32 = requests.post(Hamo29, headers=Hamo30, data=Hamo31).text

        if "true" in Hamo32:
            text4 = "Two social hours have been added successfully "
            print("")
            print(Hamo3 + text4)
        else:
            print(Hamo1 + "Error The account information is incorrect ")
    else:
        print("");
