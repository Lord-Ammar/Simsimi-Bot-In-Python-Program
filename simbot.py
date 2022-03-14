#Open Source
#Belajar Yang Bener Jan Recode Terus
#Subscribe Lah Biar Afdhol
#https://bit.ly/AmmarExecuted
#Gak Subscribe Gak Berkah:)

import requests,os,sys,time
from colorama import Fore,Back,init

#Jan Diubah Ini Buat Connect Ke Rest Api Nya:)
connect = ("Online Server")

ip = requests.get('https://api.ipify.org').text
localtime = time.asctime(time.localtime(time.time()))
server = ("api.simsimi.net")
Stats = (connect)

#Kode Warna Python
#Hijau=\033[1;92m
#putih=\033[1;97m
#abu=\033[1;90m
#kuning=\033[1;93m
#ungu=\033[1;95m
#merah=33[37;1m
#biru=\033[1;96m
#Tulisan Background Merah
#\033[1;0m\033[1;41mText\033[1;0m

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK

#Buat Tanya Main Lagi Atau Enggak
def lagigak():
	cblg = input("Back Tools? (y/n): ")
	if cblg == "y" or cblg == "Y":
		time.sleep(2)
		tanya()
	if cblg == "n" or cblg == "N":
		sys.exit
	else:
		print ("Masukin Yang Bener:)")
		time.sleep(2)
		lagigak()

#Ubah/Ganti Link Disini
def subs():
	print ("Subscribe Dulu Biar Afdhol:)")
	os.system("xdg-open https://bit.ly/AmmarExecuted")
	time.sleep(2)

def tanya():
	try:
		os.system("clear")
		logo()
		print ("")
		print ("\033[1;97m1.Chat Dengan Bot"+Fore.RED+" (""\033[1;93mActive"+Fore.RED+")")
		print (Fore.WHITE+"2.Laporkan"+Fore.RED+" (""\033[1;93mBug"+Fore.RED+")")
		print ("\033[1;97m3.Exit Tools")
		print()
		am = input("Pilih Menu: ")
		if am == "1":
			start()
		if am == "2":
			os.system("xdg-open https://wa.me/6288229683561?text=Assalamualaikum+Bang+*Laporan:*")
			lagigak()
		if am == "3":
			sys.exit
		if am == "" or am == " ":
			print ("Input Yang Bener:)")
			time.sleep(2)
			tanya()
	except KeyboardInterrupt:
		print ("Program Dihentikan")

#Ini Logo Terserah Kalo Mau Ubah
def logo():
	print ("""
\033[1;93m   _  _             \033[1;96m_________.__       __________        __           \033[1;93m  _  _
\033[1;93m__| || |__         \033[1;96m/   _____/|__| _____\______   \ _____/  |_        \033[1;93m__| || |__
\033[1;93m\   __   /\033[1;92m ______ \033[1;96m\_____  \ |  |/     \|    |  _//  _ \   __\ \033[1;92m______ \033[1;93m\   __   /
\033[1;93m |  ||  | \033[1;92m/_____/ \033[1;96m/        \|  |  Y Y  \    |   (  <_> )  |  \033[1;92m/_____/ \033[1;93m |  ||  |
\033[1;93m/_  ~~  _\       \033[1;96m/_______  /|__|__|_|  /______  /\____/|__|         \033[1;93m /_  ~~  _\\
  |_||_|                \033[1;95m \/          \/       \/                    \033[1;93m   |_||_|"""+Fore.RED)
	print ("            \t["+Back.WHITE+Fore.BLACK+"Copyright By ©AmmarBN ©2022 Sunday 13 March \033[00m"+Fore.RED+"]")
	print("")
	print ("        \033[1;90m•\033[1;97m Time: \033[1;92m"+localtime)
	print ("        \033[1;90m•\033[1;97m Stoped: \033[1;92mCTRL c")
	print ("        \033[1;90m•\033[1;97m Your Ip: \033[1;92m"+ip)
	print ("	\033[1;90m•\033[1;97m Tools Server: \033[1;92m"+server)
	print ("        \033[1;90m•\033[1;97m Status In Server: \033[1;92m"+Stats)

#Dibagian Ini Jangan Diubah Ngab Nanti Eror
def start():
	try:
		os.system("clear")
		subs()
		logo()
		print()
		ha = input("\033[1;96mNama Kamu: \033[1;92m")
#Jangan Ubah Link Api Dibawah
		#https://api.simsimi.net/bg/?text={me}&lc=id (not working)
		#https://api.simsimi.net/v2/?text={me}&lc=id (working)
		while True:
		    me = input(Fore.WHITE+ha+':\033[1;92m ')
		    url = f'https://api.simsimi.net/v2/?text={me}&lc=id'
		    response = requests.get(url)
		    if response.status_code == 200:
		        print('\033[1;97msimi bot: \033[1;92m', response.json().get('success'))
		    else:
		        print('bad respon ')
	except KeyboardInterrupt:
		print ("Program Dihentikan")
if __name__=="__main__":
	tanya()
