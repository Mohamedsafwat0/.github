import requests
import hashlib
import requests
import requests,os,sys,time,pyfiglet
import webbrowser
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
print(F+"---------  Welcome My Script {500 MG Orange} --------")
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
number=input(Y+"Enter Your Number : \033[1;33m")
print()
time.sleep(1.5)
password=input(Y+"Enter Your Password : \033[1;33m")
print()
time.sleep(1.5)
print(B+"="*60)
print()
time.sleep(1.5)
url = 'https://services.orange.eg/SignIn.svc/SignInUser'
header ={
"net-msg-id": "61f91ede006159d16840827295301013",
"x-microservice-name": "APMS",
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "160",
"Host": "services.orange.eg",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.14.9",
}
data = '{"appVersion":"7.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (number,password)
r=requests.post(url,headers=header,data=data).json()
#print(r)
userid=r["SignInUserResult"]["UserData"]["UserID"]
print("Wait Pro....")
print()
urlo = "https://services.orange.eg/GetToken.svc/GenerateToken"
hdo = {"Content-type":"application/json", 
  "Content-Length":"78", 
  "Host":"services.orange.eg"
   , "Connection":"Keep-Alive" ,
    "User-Agent":"okhttp/3.12.1"}
datao = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' %(number,password)
ctv = requests.post(urlo,headers=hdo,data = datao).json()["GenerateTokenResult"]["Token"]
key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
htv=(str(hashlib.sha256((ctv+key).encode('utf-8')).hexdigest()).upper())
url2="https://services.orange.eg/APIs/Promotions/api/CAF/Redeem"
data2='{"Language":"ar","OSVersion":"Android7.0","PromoCode":"رمضان كريم","dial":"%s","password":"%s","Channelname":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF"}' %(number,password)
header2={
"_ctv": ctv,
"_htv": htv,
"UserId": userid,
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "142",
"Host": "services.orange.eg",
"Connection": "Keep-Alive",
"User-Agent": "okhttp/3.14.9",
}
da=data2.encode('utf-8')
response = requests.post(url2, headers=header2, data=da).json()

if 'ErrorDescription' in response:
    if response['ErrorDescription'] == 'Success':
        print(F+"524 MB added successfully ")
    elif response['ErrorDescription'] == 'User is redeemed before':
        print(X+"The offer is not currently available to you ")
    else:
        print(Z+"حدث خطأ، حاول مرة أخرى")
else:
    print(Z+"حدث خطأ غير متوقع، حاول مرة أخرى")
    

