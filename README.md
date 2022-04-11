# NuremX - Apex Legends
NuremX is a cheat for Apex Legends that uses Nurel AI Training and Model Detection, We have spent over 4000 Screenshots and 200 Text Definitions to train a AI to detect enimies with
customizable configurations and code, We professionally trained a AI to detect enimies and it works flawless.
![alt text](https://github.com/Zurek0x/NuremX/blob/main/media/header.jpg)

# Public-Test
NuremX is a public test cheat, It is not fully working and will still be constantly updated, As the game updates and so does the script there is still a lot of issues to be fixed.

![alt text](https://github.com/Zurek0x/NuremX/blob/main/media/Screenshot_6.png)

# Update_Check Function
The program will auto check for updates from the github repo' using URLLIB3, Upon a version change the **ver.txt** file & **current_ver** (str) in the script will be changed, If the versions do not match in any-case scenario the program will forcefully become un-usable until a update to the program comes, You must re-clone the repo' and **pip install -r requirements.txt** for the leatest requirements, This option is unable to be turned off and you must update to keep up with newer optimizations or newer content.

# What Is Nurel Network & AI Training?
NuremX Uses YOLOv5 AI Training and AI Datasets, We have trained a professional AI to recognize enimies and entities and soon items and or objects, This is a advanced cheat, There is no Memory Hooking or Hex Editing or even Process Hooking, Everything comes straight from your display and it will recognize the enimies and automatically aim at them and display there position. We hope to build onto this a lot more and find that Process Hooking and Memory Hooking/Editing is a long process especially when you have a Anti-Cheat in the way of your path to making a sucsessful cheat program or script.
We don't want people to take this as it "is" a cheat or Aim-Assist but something you can learn off of, We think that AI Training and Nurel Networks are great and a good way to train AI to do human tasks, We are starting to see in 2022+ that AI is becoming more powerful and as computers become more powerful we can output almost the same power as a human brain.

# Note About Clones & Rats
Un-official sources of our project may show up in a form of a Fork or post from a random person or friend, Never trust it. Always download the code and program from our github page ( https://github.com/Zurek0x/NuremX ) And don't run/download any code that doesn't come from this main repository. If you come accross a Copy of our project with malicious code or just a straight Clone/Fork of our project DO NOT TRUST IT, If we see a fork of our project we will implement the update into our current script as a UPDATE.

# Notice About Performance
This script uses A LOT of RAM/CPU/GPU Power, You must have at least 3 GB of DDR3 Ram dedicated to the script, Note that also anything lower peformance then a GTX 1080 TI will have delayed peformance and have a lower Frame Count You also want at least a 3Ghz (or more) CPU with more then 3 Cores Minimum. 

# Cheat Features
> Script Features
> * Lots of customization options
> * Better support for Aim Assist
> * GPU/Cuda Utilization
> * Ryzen/AMD/Intel CPU Support
> * Windows 10/11 & Debian Linux Support
>
> Bypassing Features
> > These bypassing features doesn't actually bypass the anti-cheat but spoofs it so it doesn't get saved by the anti-cheat and later get auto flagged when detected as a running process or window or file.
> * UUID Spoofing (Spoofs Title Window & Command Window)
> * Arduino Compatible (Coming Soon, Requires Capture Card)
> * Windows.NT Hooking (Hiding script behind {windows command processor} and {explorer.exe} )
> * Icon spoofing (Spoofing icon of program)
>
> Cheat Features
> * Aim-Assist (Customizable With Configuration)
> * Overlay Status and FOV
> * Player ESP
> * Customizable Dataset

# Configuration
> you can edit the config using the "configuration_settings.ini" file
> * 0 = Off   |    1 = On
> * welcome_notif = 0/1 | Display welcome notification at startup
> * size_of_window = 0/1000
> * confidence_threshold = 0.10/0.99  |  Confidence Threshold  |  0.01 = No Detection Strictness (Can Detect Non-Players)  |  0.99 = Strict Detection (Must Affirm its a enemy)
> > Best Confidence Threshold / DECENT > 0.12 / BEST > 0.21 / ALSO BEST > 0.34 / 0.45 / 0.55
> * nms_iou = 0.10/0.99  |  Keep same as confidence_threshold ALWAYS
> * mouse_delay = 0.0001/0.9999  |  The delay at wich your mouse moves
> * pixel_increse = 1/20  |  The speed at which your crosshair/mouse moves at (Sensitivity)
> > Best Pixel Increse / OK > 3 / GOOD > 6 / BEST > 8 / ALSO BEST > 10-12 / 14 / 16
> * status_overlay = 0/1  |  1 = On  /  0 = Off
> * overlay_resolution_X = 1/4000  |  Set overlay resolution by the X-Axis
> * overlay_resolution_Y = 1/4000  |  Set overlay resolution by the Y-Axis
> * promote = 0/1
> > Either turn on or off discord rich presence to support the project!

# Public Source
Our code is public source and free to use/edit (But do not sell, We have a liense) You may edit our code (Under A Fork of the project, By obligaitons of our license you may not distribute non-approved / tampered code unless it has been approved as a FORK of our project)
![alt text](https://github.com/Zurek0x/NuremX/blob/main/media/Screenshot_5.png)

# How to install and use
```
Required Pieces Of Software:
[Python 3.9 Or Later] > https://www.python.org/downloads/
(make sure to add your version of python to PATH) > https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png
(it should ask you in the installer.)
Once done do the following.

[installing and running]
After installing python and making sure to follow images as they say do the following.
1. Open CMD as administrator
2. run the command " python ", If the command works a python IDE should open if so then continue!
(If it doesn't then check the video "How To Add Python To PATH" Also make sure you installed Python first)
3. Close and re-open CMD as administrator
4. run the command " pip ", If a bunch of commands and help info comes up then continue!
(If it doesn't then check the video "How To Install PIP for python" Also make sure you intsalled python)
5. next run the "setup.bat" file in "open-source" folder.
6. after the setup has completed then run the " run.bat " file / If on windows
(Linux users can just install the requirements.txt and then run NuremX.py using Python Command)
7. wait for the script to startup and done! 


Help Videos.
How To Install PIP for Python > https://youtu.be/Ko9b_vC6XY0
How To Add Python to PATH > https://youtu.be/Y2q_b4ugPWk
```

# Change-Log
> Version 2.1
> * Changed aimbot trigger key to 'X' (0x58) on winuser.h module
>
> Version 2.0
> * Added overlay_resolution function to overlay
> * Added overlay_resolution_x to configuration file
> * Added overlay_resolution_y to configuration file
>
> Version 1.9
> * Added RICH_PRESENCE Sponsorship
> * Fixed requirements.txt broken modules
>
> Version 1.8
> * Changed version listing from Float to Int.
> * Added status_overlay function to script
> * Added status (enabled / disabled) overlay on top left of screen
>
> Version 1.7
> * Fixed Update_Check Function (Wasn't Checking Properly)
>
> Version 1.5.9
> * Added Update_Check Function to check for updates (Does Not Auto Update)
> 
> Version 1.5.8
> * Updated Dataset to a more optimized dataset with more AI Training
> * Updated Dataset loading to be more optimized
> 
> Version 1.5.5
> * Full & Tested Intel/AMD/Ryzen CPU Support
> * Full & Tested RTX Core utilization & CUDA
> * RTX Cores are not utilized at this time, This is soon to come.
> 
> Version 1.4.5
> * Added Display of config options in UI
> * Added more configurable options in .INI file
> * Added better script optimization
> 
> Version 1.4.2
> * Added "Configparser" Module
> * Added configurable options from .ini file
> * Added Pixel Increse (Sensitivity) configuration option
> 
> Version 1.3.6
> * Fixed script bugs
> * Added RAM Optimizations (From 5-6Gb to 2-3Gb)
> * Better GPU/CUDA Utilization
> 
> Version 1.3
> * Fixes to script features and bugs
> * Minor UI Changes
> 
> Version 1.0
> * Added source to github.com
> * Published code to public

# Screenshots
![alt text](https://github.com/Zurek0x/NuremX/blob/main/media/Screenshot_7.png)
![alt text](https://github.com/Zurek0x/NuremX/blob/main/media/Screenshot_8.png)
![alt text](https://github.com/Zurek0x/NuremX/blob/main/media/Screenshot_9.png)


# Credits
> * Zurek0x (Developing & Testing)
> * tyl (Developing & Testing)
> * KurkMF (Development Process & Testing)

# Моим русским зрителям
Поскольку я вижу много людей, скачивающих и использующих мою программу из Российской Федерации, позвольте напомнить вам, что поддержка русского языка еще не добавлена, мы добавим это позже когда-нибудь.
