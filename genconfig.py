import os
import time


def main():
    print("Configuration Generation Assistant")

    print("Checking for existing configuration file...")
    print(" ")
    if os.path.exists("preferences.toml"):
        print("Configuration file already exists! Try editing it instead.")
    else:
        print("Configuration file not found. Do you want to create one?")
        choice = input("Enter 'y' to create, 'n' to cancel: ")
        if choice.lower() == "y":
            tomlcontents = """#THIS IS A CONFIGURATION FILE! IT IS REQUIRED FOR OSU SERVER SELECTOR TO WORK.
    #Read the information in the GitHub repository for more information on each of the options.

    [location]
    #Leave empty to start with default options. Make sure to include the osu! executable in the string.
    gamelocation = ""

    [server]
    #Leave empty to start with default options. Do not include the "https://" part of the URL.
    bancho = ""

    [launchflags]
    #Leave empty to start with default options. Define flags like "-repair" or "-compatibility"
    flags = ""

    [preferences]
    #Defines if you want to not be asked what server you're trying to launch. True/False option.
    autolaunchserver = false
    """
            f = open("preferences.toml", "x")
            f.write(tomlcontents)
            f.close()
            print(
                "Generation complete. You should now see 'preferences.toml' in the program directory."
            )
            print(" ")
        else:
            print("File creation cancelled. Closing in 3 seconds.")
            print(" ")
            time.sleep(3)
            exit()


if __name__ == "__main__":
    main()
