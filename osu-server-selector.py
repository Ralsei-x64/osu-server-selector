# Built by a human with love.
# My code sucks, but it's my first py project.
# Import python modules
import os
import platform
import subprocess
import time
import tomllib

# Import toml gen script for config
import genconfig

# Show Title
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
print(" ")

# TOML Parsing Stuff
if os.path.exists("preferences.toml"):
    with open("preferences.toml", "rb") as f:
        data = tomllib.load(f)
else:
    genconfig.main()
    with open("preferences.toml", "rb") as f:
        data = tomllib.load(f)

gamelocation = data["location"]["gamelocation"]
banchoserver = data["server"]["bancho"]
autolaunchserver = data["preferences"]["autolaunchserver"]
flags = data["launchflags"]["flags"]
current_directory = os.getcwd()
useraccount = os.getlogin()

# Define OS to print messages
if platform.system() == "Linux":
    print("Welcome to osu! server selector!")
elif platform.system() == "Windows":
    print("Welcome to osu! server selector!")
elif platform.system() == "Darwin":
    print("macOS is not supported. Sorry!")
    time.sleep(3)
    quit()

print(" ")

# Handling Game Location and TOML File Info
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

# print(launchcommand)  # comment out when not testing
if autolaunchserver == True:
    print("Launching osu! with the server: " + launchbanchoserver)
    launchcommand = launchlocation + " " + final_launchbanchoserver + launchflags
else:
    server_URL = input("Type server URL to launch: ")
    if server_URL == "":
        launchcommand = launchlocation
    else:
        launchcommand = launchlocation + " " + "-devserver " + server_URL + launchflags

print("Launching game...")
subprocess.run(launchcommand)  # Launches the game with the selected server/options.
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
