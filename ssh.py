# coding: utf-8

"""
Even if you want to enc it's free, I can't
type: git pull

coded by myohtetpaing2021 ID
"""

from os import system
import re, random, sys, time, platform
try:
	from bs4 import BeautifulSoup as par
	from requests import *
except:
	exit("\n\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ALL MODULE NOT INSTALLED\n PLEASE READ README.md\n")

if platform.python_version().split(".")[0] != "3":
	exit("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] TYPE: python "+sys.argv[0])

def Make_ssl(id, cookies, user, pw, server):
	data = {"serverid":id,"username":user,"password":pw}
	agent = open("ua.txt","r").read()
	acak = random.choice(agent.split("\n"))
	head = {"Host":"www.speedssh.com","Connection":"keep-alive","Accept":"*/*","Origin":"https://www.speedssh.com","X-Requested-With":"XMLHttpRequest","User-Agent":acak,"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Referer":server,"Accept-Encoding":"gzip, deflate","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	posd = post("https://www.speedssh.com/create-ssl-30-days.php", headers=head, data=data, cookies={"PHPSESSID":cookies}).text
	if "Your Account has been successfully created !" in posd:
		print("  \x1b[1;91m>>> \x1b[1;97mACCOUNT \x1b[1;92mSUCCEED \x1b[1;97mCREATED")
		print("  \x1b[1;91m> \x1b[1;97mUSERNAME \x1b[1;91m:\x1b[1;92m "+re.search("Username\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;97mPASSWORD \x1b[1;91m:\x1b[1;92m "+re.search("Password\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;97mHOST     \x1b[1;91m:\x1b[1;92m "+re.search("Host\sIP\s\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;97mPROTOCOL \x1b[1;91m:\x1b[1;92m SSL/TLS")
		print("  \x1b[1;91m> \x1b[1;97mSSL PORT \x1b[1;91m:\x1b[1;92m 443")
		print("  \x1b[1;91m> \x1b[1;97mOPENSSH PORT  \x1b[1;91m:\x1b[1;92m 22,109,110")
		print("  \x1b[1;91m> \x1b[1;97mDROPBEAR PORT \x1b[1;91m:\x1b[1;92m 444,143,80")
		print("  \x1b[1;91m> \x1b[1;97mCREATE ACCOUNT\x1b[1;91m:\x1b[1;92m "+re.search("on : (.*?)<br>", str(posd)).group(1).replace("-", " ").upper())
		print("  \x1b[1;91m> \x1b[1;97mEXPIRE ACCOUNT\x1b[1;91m:\x1b[1;92m "+re.search("expire on (.*?).<br>", str(posd)).group(1).replace("-", " ").upper()+"\n")
	elif "Username already exists !" in posd:
		exit(" \x1b[1;97m[\x1b[1;91m*\x1b[1;97m] USERNAME HAS BEEN CREATED WITH PERSON\n")
	else:
		exit(" \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] YOU HAVE CREATED ACCOUNT THROUGHOUT THE LIMITS\n")

def Make_ssh(id, cookies, user, pw, server):
	data = {"serverid":id,"username":user,"password":pw}
	agent = open("ua.txt","r").read()
	acak = random.choice(agent.split("\n"))
	head = {"Host":"www.speedssh.com","Connection":"keep-alive","Accept":"*/*","Origin":"https://www.speedssh.com","X-Requested-With":"XMLHttpRequest","User-Agent":acak,"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Referer":server,"Accept-Encoding":"gzip, deflate","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	posd = post("https://www.speedssh.com/create-ssh-30-days.php", headers=head, data=data, cookies={"PHPSESSID":cookies}).text
	if "Your Account has been successfully created !" in posd:
		print("  \x1b[1;91m>>> \x1b[1;97mACCOUNT \x1b[1;92mSUCCEED \x1b[1;97mCREATED")
		print("  \x1b[1;91m> \x1b[1;97mUSERNAME \x1b[1;91m:\x1b[1;92m "+re.search("Username\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;97mPASSWORD \x1b[1;91m:\x1b[1;92m "+re.search("Password\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;97mHOST     \x1b[1;91m:\x1b[1;92m "+re.search("Host\sIP\s\s\s:\s(.*?)<br>", str(posd)).group(1))
		print("  \x1b[1;91m> \x1b[1;97mPROTOCOL \x1b[1;91m:\x1b[1;92m TCP AND UDP")
		print("  \x1b[1;91m> \x1b[1;97mSSL PORT \x1b[1;91m:\x1b[1;92m 444")
		print("  \x1b[1;91m> \x1b[1;97mOPENSSH PORT  \x1b[1;91m:\x1b[1;92m 22,109")
		print("  \x1b[1;91m> \x1b[1;97mDROPBEAR PORT \x1b[1;91m:\x1b[1;92m 443,80,143")
		print("  \x1b[1;91m> \x1b[1;97mCREATE ACCOUNT\x1b[1;91m:\x1b[1;92m "+re.search("on : (.*?)<br>", str(posd)).group(1).replace("-", " ").upper())
		print("  \x1b[1;91m> \x1b[1;97mEXPIRE ACCOUNT\x1b[1;91m:\x1b[1;92m "+re.search("expire on (.*?).<br>", str(posd)).group(1).replace("-", " ").upper()+"\n")
	elif "Username already exists !" in posd:
		exit(" \x1b[1;97m[\x1b[1;91m*\x1b[1;97m] USERNAME HAS BEEN CREATED WITH PERSON\n")
	else:
		exit(" \x1b[1;97m[\x1b[1;91m+\x1b[1;97m] YOU HAVE CREATED ACCOUNT THROUGHOUT THE LIMITS\n")

class SSL_TLS:
	def __init__(self):
		self._name = 0
		self.link = []

	def Chek(self):
		self.cek = par(get("https://speedssh.com/ssl-server-30-days").text, "html.parser")
		for one in self.cek.find_all("div", attrs={"class":"plan-hp"}):
			for two in one.find_all("h1"):
				self._name += 1
				print("  \x1b[1;96m{\x1b[1;92m"+str(self._nom)+"\x1b[1;96m}\x1b[1;97m "+two.text)
			for url in one.find_all("a", attrs={"class":"order-plan"}):
				self.link.append(url.get("href"))

		self.select = input("\x1b[1;91m+-----------------------------------+\n  \x1b[1;97m>>> ")
		while self.select == "":
			print(" \x1b[1;91m >>>\x1b[1;97m WHAT'S REALLY HOT\x1b[1;91m!")
			self.select = input("  \x1b[1;97m>>> ")
		try:
			checkin = self.link[int(self.select) - 1]
		except (ValueError, IndexError):
			exit(" \x1b[1;97m[\x1b[1;91m!\x1b[1;97m] PLEASE ENTER THE NUMBER BRO.")
		cek_2 = par(get(chekin).text, "html.parser")
		if cek_2.find("div", class_="progress-bar progress-bar-danger") is None:
			serverid = cek_2.find('input', {"type":"hidden"}).get("value")
			cookie = re.search("PHPSESSID=(\w+)\sfor", str(get(chekin).cookies)).group(1)
			print("\x1b[1;91m+-----------------------------------+")
			user = input("  \x1b[1;91m==> \x1b[1;97mSET USERNAME:\x1b[1;96m ")
			pasw = input("  \x1b[1;91m==> \x1b[1;97mSET PASSWORD: \x1b[1;96m")
			print("\x1b[1;91m+-----------------------------------+")
			Make_ssl(serverid, cookie, user, pasw, chekin)
		if cek_2.find("div", class_="progress-bar progress-bar-danger") is not None:
			exit("  \x1b[1;97m[\x1b[1;91m#\x1b[1;97m] ACCOUNT NOT AVAILABLE\n      PLEASE SELECT SERVER OTHER..\n")
			time.sleep(2)
			system('python '+sys.argv[0])

class SSH:
	def __init__(self):
		self._num = 0
		self.link = []

	def Chek(self):
		self.cek = par(get("https://speedssh.com/ssh-server-30-days").text, "html.parser")
		for one in self.cek.find_all("div", attrs={"class":"plan-hp"}):
			reg = re.findall("<h1>(.*?)</h1>", str(one))
			for judul in reg:
				self._num += 1
				print("  \x1b[1;96m{\x1b[1;92m"+str(self._num)+"\x1b[1;96m}\x1b[1;97m "+title)
			for url in one.find_all("a", attrs={"class":"order-plan"}):
				self.link.append(url.get("href"))

		self.select = input("\x1b[1;91m+-----------------------------------+\n  \x1b[1;97m>>> ")
		while self.select == "":
			print(" \x1b[1;91m >>>\x1b[1;97m WHAT'S REAL\x1b[1;91m!")
			self.select = input("  \x1b[1;97m>>> ")
		try:
			checkin = self.link[int(self.select) - 1]
		except (ValueError, IndexError):
			exit(" \x1b[1;97m[\x1b[1;91m!\x1b[1;97m] PLEASE ENTER THE NUMBER BRO.")
		cek_2 = par(get(chekin).text, "html.parser")
		if cek_2.find("div", class_="progress-bar progress-bar-danger") is None:
			serverid = cek_2.find('input', {"type":"hidden"}).get("value")
			cookie = re.search("PHPSESSID=(\w+)\sfor", str(get(chekin).cookies)).group(1)
			print("\x1b[1;91m+-----------------------------------+")
			user = input("  \x1b[1;91m==> \x1b[1;97mSET USERNAME:\x1b[1;96m ")
			pasw = input("  \x1b[1;91m==> \x1b[1;97mSET PASSWORD: \x1b[1;96m")
			print("\x1b[1;91m+-----------------------------------+")
			Make_ssh(serverid, cookie, user, pasw, checkin)
		if cek_2.find("div", class_="progress-bar progress-bar-danger") is not None:
			exit("  \x1b[1;97m[\x1b[1;91m#\x1b[1;97m] ACCOUNT NOT AVAILABLE\n      PLEASE SELECT SERVER OTHER..\n")
			time.sleep(2)
			system('python '+sys.argv[0])

def Menu():
	print("""
   \x1b[1;93m ╔ dosed
    ║  ╠╦╝║╣ ╠═╣ ║ ║╣   ╚═╗╚═╗╠═╣
    ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝  ╚═╝╚═╝╩ ╩
\x1b[1;97m https://github.com/myohtetpaing2021
\x1b[1;91m+-----------------------------------+
\x1b[1;96m  {\x1b[1;92m01\x1b[1;96m} \x1b[1;97mCREATE SSL/TLS MONTHLY
\x1b[1;96m  {\x1b[1;92m02\x1b[1;96m} \x1b[1;97mCREATE SSH MONTHLY
\x1b[1;96m  {\x1b[1;91m00\x1b[1;96m} \x1b[1;91mEXIT PROGRAM
\x1b[1;91m+-----------------------------------+""")
	select = input("  \x1b[1;97m>>> \x1b[1;92m")
	while select == "":
		print(" \x1b[1;91m >>>\x1b[1;97m WHAT'S REAL\x1b[1;91m!")
		select = input("  \x1b[1;97m>>> \x1b[1;92m")
	if select in ("1","01"):
		nice = SSL_TLS
	elif select in ("2","02"):
		nice = SSH
	elif select in ("0","00"):
		exit("\x1b[1;91m+----------------------------------+\n \x1b[ 1;97mTHANK YOU FOR USING MY TOOLS\n")
	else:
		exit(" \x1b[1;91m >>> \x1b[1;97mSORRY MENU \x1b[1;91m'\x1b[1;97m"+select+"\x1b[1;91m'\x1b[1;97m NO FOUND\n")
	print("\x1b[1;91m+-----------------------------------+")
	nice().Chek()

if __name__=="__main__":
	system('clear')
	try:
		Menu()
	except Exception as er:
		exit("\n \x1b[1;97m [\x1b[1;91m!\x1b[1;97m] ERROR: "+str(er))
