# osu-server-selector

CLI osu! server switcher built with python! This is my first python project which took me around 8-10 hours to learn and get working.
 
 **Warning: This utility is built for Windows. It might work on Linux but I'm 100% certain it will not work on macOS**

## 🕹️ Getting Started
You can download the script by using 'git clone' or downloading the code as a zip through github.

This utility is rather simple, you can configure it to your liking via the `preferences.toml` file provided in the utility's folder. By default, you will be asked what server you want to launch osu! with. Leaving the field blank, the game will start normally.

### Requirements
- Any Windows version that supports osu! stable and Python 3.14 (Windows 8.1 and above)
- Python 3.14 installed on your system
- osu! installed. If you've installed it to a custom directory, specify it in the `[location]` section of the preferences file.
- Enough technical knowledge to use a computer.

## ⚙️ How to configure

### Preferences.toml
The preferences.toml file is broken into the following four sections:
1.  `[location]` In the gamelocation line, you can add a custom game directory (including the osu!.exe at the end). Example: `gamelocation = "G:\\Games\\osu!\\osu!.exe"`
2. `[server]` Allows us to specify where we want osu! to connect to. Aka, the thing we're here for. We can for example point it to `bancho = "halcyon.moe"`and it'll connect to the halcyon servers. Do not include the `"https://"` part of the URL as osu! does not like it.
3. `[launchflags]` Not functional yet. This one is a bit of an extra, but we can parse custom flags like `-repair` before osu! executes. An example is `flags = "-repair"`
4. `[preferences]` Dictates if you want to launch the server without any interruptions on the console. `autolaunchserver = "False"` means you will be asked to input a server URL to launch with. `autolaunchserver = "True"` will skip that and use the parameters in the preferences file.

This file is required for the python script to start correctly. You will get an error if it is not detected in the directory. To open it with notepad you have two options: changing the extension or forcing it to open with notepad. 
1. To change the extension, rename the file from `.toml` to `.txt` and open it normally. The file should load like a normal txt file.
2. To force it to open, we can right click on the file > open with> Notepad. It should also work this way.

## 🏃‍♂️‍➡️ Usage
### Running the script
The script must run inside its folder to work properly. If you want to run it outside its folder, we can create a shortcut to place in any directory. However, running the script is as easy as double clicking on the python file. An installation of python is required for this to work.

In your preferences, if `autolaunchserver = "False"`, you will be asked to enter the bancho server you would like to start up with. You can leave it blank if you wish to start up with ppy servers. For entering servers, you only need to type in the URL (excluding `https://`) and press enter. 

### For other operating systems...
I built this script mostly tailored for Windows. It could perhaps be edited for other operating systems but for now I've built it for Windows because of osu! being Windows only.

 Linux can run the script just fine but will return an error once it cannot find the osu! executable. We can get around this by using WINE to run osu! and the script, but this has its own drawbacks. osu-wine provides its own way of switching servers and is probably more robust.

macOS... Uhh use lazer I guess..

## 📖 Acknowledgements

**Python & their documentation** for obviously making it possible and teaching me how to do stuff.
**Stackoverflow threads** for teaching me some stuff.
**Google's Gemini** for helping me learn how toml is parsed.
**Peppy** *you know why..*

