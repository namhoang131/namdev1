from builtins import all,exec,format,id,print,int,range,set,str,open,quit
exec('')
import os
try:
	import requests,colorama,prettytable
except:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip install prettytable')
import threading,requests,ctypes,random,json,time,base64,sys,re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init,Fore
from urllib.parse import urlparse,unquote,quote
from string import ascii_letters,digits
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
lam = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
edit = vang+"]"+trang+"["+do+"[⟨⟩]"+trang+"]"+vang+"["+trang+" ➩ "+luc
edit1 = trang+"["+do+"[⟨⟩]"+trang+"]"+trang+" ➩ "+luc
# =======================[ NHẬP KEY ]=======================
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(0)
banner=f"""
            \033[1;36m╭─⋞─────────────────────────────────────────────────────╮
            \033[1;31m███╗   ██╗ █████╗ ███╗   ███╗    ██████  ███████╗██╗   ██╗          
            \033[1;32m████╗  ██║██╔══██╗████╗ ████║    ██╔══██╗██╔════╝██║   ██║          
            \033[1;33m██╔██╗ ██║███████║██╔████╔██║    ██║  ██║█████╗  ╚██╗ ██╔╝          
            \033[1;34m██║╚██╗██║██╔══██║██║╚██╔╝██║    ██║  ██║██╔══╝   ╚████╔╝           
            \033[1;35m██║ ╚████║██║  ██║██║ ╚═╝ ██║    ██████╔╝███████╗  ╚██╔╝            
            \033[1;36m╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   
            \033[1;34m Youtube : \033[1;37mhttps://youtube.com/@NamTool1
            \033[1;34m Nhóm Zalo : \033[1;37mhttps://zalo.me/g/kfmgqm225
            \033[1;34m Facebook   : \033[1;37mhttps://facebook.com/nam.nhn131 
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯ 
            \033[1;31m               TOOL ENCODE BY NAMDEV
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
print(f"{trang} ➩ Ngày{trang} : {do}{ngay_hom_nay}{vang} |{luc} Tháng{trang}: {do}{thang_nay} {vang}| {luc}Năm{trang}: {do}{nam_}{vang} | {luc}Thời Gian: {do}{time}")
print(f'{trang} ➩ IP Hiện Tại Của Bạn : {vang}{ip}')
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
print("\033[1;35m╔══════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[1] \033[1;32mVÀO TOOL ENCODE IMPOSTOR             \033[1;35m  ║ ")
print("\033[1;35m╚══════════════════════════════════════════════╝")
print("\033[1;35m╔══════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[2] \033[1;32mVÀO TOOL ENCODE 16 CHẾ ĐỘ              \033[1;35m║ ")
print("\033[1;35m╚══════════════════════════════════════════════╝")
print("\033[1;35m╔══════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[3] \033[1;32mVÀO TOOL ENCODE MARSHAL                \033[1;35m║ ")
print("\033[1;35m╚══════════════════════════════════════════════╝")
print("\033[1;35m╔══════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[4] \033[1;32mVÀO TOOL ENCODE BERSERKER              \033[1;35m║ ")
print("\033[1;35m╚══════════════════════════════════════════════╝")
print("\033[1;35m╔══════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[5] \033[1;32mVÀO TOOL ENCODE SPECTER                \033[1;35m║ ")
print("\033[1;35m╚══════════════════════════════════════════════╝")
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[0] \033[1;32mQUAY LẠI MENU TOOL          \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
chon = int(input('\033[1;33mnhn\033[1;95m@\033[1;36mNamDev$ '))
if chon == 1 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdevtool/main/encimposter.py').text)
elif chon == 2 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdevtool/main/enc16chedo.py').text)
elif chon == 3 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdevtool/main/encmarshal.py').text)
elif chon == 4 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdevtool/main/encberserker.py').text)
elif chon == 5 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdevtool/main/encspecter.py').text)
elif chon == 0 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdevgop/main/gop.py').text)
else :
    sys.exit('Vui Lòng Chọn Đúng Chế Độ')