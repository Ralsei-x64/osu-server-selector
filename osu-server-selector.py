# Built by a human with love.
# My code sucks, but it's my first py project.

import os
import platform
import subprocess
import tomllib

current_directory = os.getcwd()
useraccount = os.getlogin()

print("""
░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
░██████╗███████╗██╗░░░░░███████╗░█████╗░████████╗░█████╗░██████╗░
██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
╚█████╗░█████╗░░██║░░░░░█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
██████╔╝███████╗███████╗███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
╚═════╝░╚══════╝╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝""")  # lmao script kitty ahh title
if platform.system() == "Linux":
    print(
        "You're using Linux! Make sure to point Server Selector to the correct osu! directory."  # The ironic part is that I wrote this on Linux and only tested it on Windows in a VM.
    )
elif platform.system() == "Windows":
    print(
        "Welcome to Server Selector! Make sure to configure this utility in the preferences.toml file."
    )
elif platform.system() == "Darwin":
    print("macOS is not supported at all. I don't even own a mac to test this with.")
    quit()


with open("preferences.toml", "rb") as f:
    data = tomllib.load(f)

gamelocation = data["location"]["gamelocation"]
banchoserver = data["server"]["bancho"]
autolaunchserver = data["preferences"]["autolaunchserver"]
flags = data["launchflags"]["flags"]

if gamelocation == "":
    launchlocation = os.path.join(
        os.path.expanduser("~"), "AppData", "Local", "osu!", "osu!.exe"
    )
else:
    launchlocation = gamelocation

if banchoserver == "":
    launchbanchoserver = "osu.ppy.sh"
else:
    launchbanchoserver = banchoserver

if flags == "":
    launchflags = ""
else:
    launchflags = flags

if launchbanchoserver == "osu.ppy.sh":
    final_launchbanchoserver = ""
else:
    final_launchbanchoserver = "-devserver " + launchbanchoserver

# print("Flags=", launchflags) #comment out when not testing
# print("Bancho Server=", launchbanchoserver) #comment out when not testing
# print("Launch Location=", launchlocation) #comment out when not testing
print("Launching osu! with the server: " + launchbanchoserver)

# print(launchcommand)  # comment out when not testing
if autolaunchserver == "True":
    launchcommand = launchlocation + " " + final_launchbanchoserver + launchflags
else:
    print("Type server URL to launch:")
    server_URL = input()
    if server_URL == "":
        launchcommand = launchlocation
    else:
        launchcommand = launchlocation + " " + "-devserver " + server_URL + launchflags

print("Launching game...")
subprocess.run(launchcommand)
quit()
# enjoy the spagetti code :333333
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣷⡄⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⢀⣾⡀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡓⠦⢄⣀⠀⠀⡼⠻⠿⢶⡄⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⡤⠤⠤⣤⣤⣴⣶⣶⠶⠶⠶⠒⠒⠂⠙⠀⠀⠀⠉⠉⠓⠲⢤⣀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠈⢿⠈⠳⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⣄⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⢀⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣟⠁⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⢈⡽⠁⠀⠀⠠⡄⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠘⡆⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⣠⠞⠀⠀⠀⠀⣠⢧⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⢹⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⡴⠃⠀⠀⠀⢠⠞⠁⠈⢣⡀⣄⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⢸⣠⡇⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢞⣓⣸⠀⢠⠰⣋⣀⣀⣳⢤⡙⢾⣟⠲⢤⣀⣠⠄⢯⠳⡀⠀⠀⠀⠸⠋⡇⠀⠀⠀⠀⠀⠀⢠⠏⠹⡄⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⣿⠀⢸⢰⠋⠀⣸⣿⣿⡆⠀⠈⠃⢤⣯⣿⡶⠾⣄⠘⡦⠀⠀⢀⣦⣿⠀⠀⠀⠀⠀⢠⠃⠀⠀⢳⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⢸⣼⣀⡀⠣⠽⠿⢃⠀⠀⠀⢾⣻⣿⡿⠀⣸⡸⠁⠀⢀⡼⡼⠉⠳⣄⠀⠀⣰⠃⠀⠀⠀⢸⠇
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠟⣷⡘⣿⣛⡁⠀⠀⠀⠀⠁⠀⠀⠀⠉⠍⠡⣶⡿⠁⠀⣠⠟⣇⡇⠀⠀⠈⢦⣰⠁⠀⠀⠀⠀⢸⠂
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠖⢻⣣⣈⣿⣤⠤⢒⠒⠦⠖⠢⠴⢄⣀⢬⣷⠞⢁⣠⠞⣡⠞⢹⡟⠀⠀⠀⠀⠃⠀⠀⠀⠀⢀⡞⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢏⣻⡶⠞⠉⠛⢉⣆⣴⡞⠻⠦⣾⢿⣊⣉⡴⣶⠁⠀⠀⠑⢄⡀⢀⢰⠋⢦⠀⠀⣠⠞⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣤⣶⣦⠀⠀⡇⠀⠀⣤⣄⠹⡟⠛⢷⠀⠁⠀⠀⠀⠀⠀⠙⠺⣏⣀⠈⢷⠚⠁⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣿⣿⣝⢿⡇⠀⣧⢠⣾⣿⣿⣿⡿⡄⢸⡄⠀⠀⠀⠀⠀⠀⠀⢸⠏⠉⠁⠈⡆⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠙⠃⠀⢸⣿⠈⠱⠟⠛⠛⠃⢹⢸⣿⡄⠀⠀⠀⣤⡀⢀⡿⠛⠓⠂⢀⢱⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣸⡀⠀⠀⠀⠀⠀⣠⢟⣸⠦⣄⣀⠀⠀⠀⠘⣸⠹⣟⡆⠀⡼⠁⠙⣾⣷⣦⣄⠀⠀⢸⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⠘⡇⠀⣀⣀⡠⠞⣱⠋⠀⠀⠀⠈⠙⢦⡀⠀⢹⡚⠉⠀⢰⠃⠀⠀⠘⣆⠀⠉⠀⠀⢸⡇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣜⠁⠀⠀⠀⠀⠙⠉⢹⣿⠁⢰⠃⠀⠀⠀⠀⠀⠀⠀⠑⣦⣬⠇⠀⢀⡏⠀⠀⠀⠀⠉⠀⠀⠀⢀⢸⡇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⡠⠟⠛⠛⠷⠂⠀⠀⠀⠀⠈⣿⢠⡇⣠⣤⣤⣤⣀⠀⠀⠀⠀⠘⣿⣶⣶⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⡞⢸⠃⠀⠀⠀
# ⠀⠀⠀⠀⠀⢀⣾⣷⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠛⡼⢉⢉⣉⣉⠛⠻⢷⣄⠀⠀⠀⣸⣯⠙⢿⣧⠀⠀⠀⠀⠀⠀⢀⡼⠁⡼⠀⠀⠀⠀
# ⠀⠀⠀⠀⡰⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⡗⠛⠛⠻⠿⣷⣦⣀⠀⠀⠀⠀⠘⢻⠀⠀⠙⠃⠀⠀⠀⠀⡠⠊⠀⢠⠃⠀⠀⠀⠀
# ⠀⣠⣖⣟⣳⣒⣆⠀⠀⠀⠀⠀⠀⠀⠀⣠⣎⠀⢸⠁⠀⠀⠀⠀⠀⠉⠉⠀⢸⠀⠀⠀⣏⠀⠀⠀⠀⠀⠠⠒⠋⠀⠀⢠⠏⠀⠀⠀⠀⠀
# ⠰⣿⣿⣶⠿⠷⣾⠃⠀⠀⠀⠀⢀⡠⠚⠁⠈⠦⡞⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⡼⠉⠁⠀⠀⠀⠀⠀⠀⠀⣠⠔⠋⠀⠀⠀⠀⠀⠀
# ⠀⠹⣦⣓⡒⠋⠉⠀⠀⠀⣀⡴⠋⠀⠀⠀⠀⡼⠁⡀⠀⠀⠀⠀⠀⠀⣠⠏⢀⣠⢾⣁⣀⣀⣀⣀⣠⠤⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⣿⣯⣿⣷⣦⢀⡴⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
