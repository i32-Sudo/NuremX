import json
import os
import os.path
import sys
import threading
import random
import string
import ctypes
import configparser
import urllib
import urllib.request

from win10toast import ToastNotifier
from pynput import keyboard
from termcolor import colored

toaster = ToastNotifier()
config = configparser.ConfigParser()

current_ver = str('v1.7')
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

def on_release(key):
    try:
        if key == keyboard.Key.f7:
            Aimbot.update_status_aimbot()
        if key == keyboard.Key.f8:
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

if __name__ == "__main__":
    title_gen = string.ascii_letters
    title_str = ''.join(random.choice(title_gen) for i in range(30))
    ctypes.windll.kernel32.SetConsoleTitleW(title_str)
    os.system('cls' if os.name == 'nt' else 'clear')
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    update_check()
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
    main()
