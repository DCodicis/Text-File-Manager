from colorama import init, Fore, Style
import random
import os

# initialize colorama
init(autoreset=True)

# list to store URLs
urls = []  # empty list to store URLs

# display program creator name and version
# Please respect the work and do not change the name
# All about the version. If there is a change in the code that was created by anyone other than "DCodicis" then do not change the version
name = "DCodicis"
vertion = "1.0.6"

# print program title
def printTitle():
    print(Style.BRIGHT + Fore.YELLOW + "\n+-----------------------+")
    print(Style.BRIGHT + Fore.YELLOW + "|" + Style.BRIGHT + Fore.CYAN + "   Made By: "+ name + "   " + Style.BRIGHT + Fore.YELLOW + "|")
    print(Style.BRIGHT + Fore.YELLOW + "+-----------------------+")
    print(Style.BRIGHT + "          v" + vertion + "\n")

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

clearScreen()
printTitle()

# create conf directory if it doesn't exist
if not os.path.exists("conf"):
    os.makedirs("conf")

# create conf/last_filename.txt file if it doesn't exist
last_filename_file = "conf/last_filename.txt"
if not os.path.exists(last_filename_file):
    with open(last_filename_file, "w") as f:
        f.write("conf/URL List.txt")

# read last filename from conf/last_filename.txt file
if os.path.exists(last_filename_file):
    with open(last_filename_file, "r") as f:
        filename = f.read().strip()
else:
    filename = ""

# read all filenames from conf/all_files.txt and filter out any that don't exist
all_files = []
all_files_file = "conf/all_files.txt"
if os.path.exists(all_files_file):
    with open(all_files_file, "r") as f:
        for line in f:
            file_name = line.strip()
            if os.path.exists(file_name):
                all_files.append(file_name)
else:
    open(all_files_file, "w").close()

# check if the most recent filename in conf/last_filename.txt exists in conf/all_files.txt and add it if it doesn't exist
with open(last_filename_file, "r") as f:
    recent_filename = f.readlines()[-1].strip()
if recent_filename not in all_files:
    all_files.append(recent_filename)
with open(all_files_file, "w") as f:
    for file_name in all_files:
        f.write(f"{file_name}\n")

# define a variable named file
file = None
while True:
    try:
        with open(filename, "r") as file:
            urls = []
            for line in file:
                line = line.strip()
                if line and ":" in line:
                    label, url = line.split(":", 1)
                    urls.append((label.strip(), url.strip()))
            clearScreen()
            printTitle()
            print(Style.BRIGHT + Fore.GREEN + "URLs loaded from file successfully!\n")
            break
    except FileNotFoundError:
        # display error message if file not found
        print("Welcome to .txt meneger. If you want to create a file, follow the instructions\n")
        response = input(Style.BRIGHT + Fore.YELLOW + "To name your first file write 'y' -->: ")
        if response.lower() == "y":
            while True:
                new_filename = input(Style.BRIGHT + Fore.YELLOW + "\nEnter a new filename (include .txt): ")
                if not new_filename.endswith(".txt"):
                    print(Style.BRIGHT + Fore.RED + "\nThe filename must end with '.txt'!")
                elif os.path.exists(new_filename):
                    clearScreen()
                    printTitle()
                    print(Style.BRIGHT + Fore.RED + "\nThe file already exists!")
                else:
                    filename = new_filename
                    with open(last_filename_file, "w") as f:
                        f.write(filename)
                    try:
                        with open(filename, "w") as file:
                            for url in urls:
                                file.write(f"{url[0]}: {url[1]}\n")
                    except FileNotFoundError:
                        print(Style.BRIGHT + Fore.RED + f"\n{filename} file not found!\n")
                    break
        else:
            clearScreen()  
            printTitle()
            filename = "conf/URL List.txt"
            print(Style.BRIGHT + Fore.YELLOW + "Using default filename 'URL List.txt'.\n")

def update_all_files():
    all_files_file = "conf/all_files.txt"
    if os.path.exists(all_files_file):
        with open(all_files_file, "r") as f:
            all_files = [line.strip() for line in f.readlines()]
        new_all_files = []
        for file_name in all_files:
            if os.path.exists(file_name) and file_name.endswith(".txt"):
                new_all_files.append(file_name)
            else:
                print(Style.BRIGHT + Fore.YELLOW + f"'{file_name}' not found! Removing from the list of available files.\n")
        with open(all_files_file, "w") as f:
            for file_name in new_all_files:
                f.write(f"{file_name}\n")
    else:
        open(all_files_file, "w").close()

    # check for any new .txt files in the directory and add them to all_files.txt
    for file_name in os.listdir():
        if file_name.endswith(".txt") and file_name not in new_all_files:
            new_all_files.append(file_name)
            with open(all_files_file, "a") as f:
                f.write(f"{file_name}\n")
                print(Style.BRIGHT + Fore.GREEN + f"\n'{file_name}' added to the list of available files.\n")
                printTitle()

def set_last_filename(filename):
    # This function sets the value of last_filename.txt to filename
    with open("conf/last_filename.txt", "w") as f:
        f.write(filename)




# main loop
while True:

    set_last_filename(filename)
    update_all_files()
    # display menu options
    print(Style.BRIGHT +"You are in: " + Fore.YELLOW+ filename)
    print(Style.BRIGHT + "\nMENU:\n")
    print(Style.BRIGHT + Fore.CYAN + "1. Add URL")
    print(Style.BRIGHT + Fore.CYAN + "2. Add New .txt File")
    print(Style.BRIGHT + Fore.CYAN + "3. Remove URL")
    print(Style.BRIGHT + Fore.CYAN + "4. Show All URLs")
    print(Style.BRIGHT + Fore.CYAN + "5. Change URL List")
    print(Style.BRIGHT + Fore.CYAN + "6. Remove .txt file")
    print(Style.BRIGHT + Fore.CYAN + "\n7. Exit\n")

    choice = input(Style.BRIGHT + "Enter your choice (1-7): ")
    print("\n\n\n\n")


    if choice == "1":
        clearScreen()
        printTitle()

        # add a new URL to the list
        url = input(Style.BRIGHT + "Enter a URL: ")
        label = input(Style.BRIGHT + "Enter a label for the URL: ")
        urls.append((label, url))  # add the URL and label as a tuple

        # save URLs to file
        if urls:
            with open(filename, "w") as file:
                for url in urls:
                    file.write(f"{url[0]}: {url[1]}\n")
        clearScreen()
        printTitle()
        print(Style.BRIGHT + Fore.GREEN + "\nURL added successfully!\n")


    elif choice == "2":
        clearScreen()
        printTitle()

        # add a new URL list
        while True:
            filename = input(Style.BRIGHT + "Enter a filename for the new .txt file (include '.txt' extension): ")
            if filename in last_filename_file:
                clearScreen()
                printTitle()
                print(Style.BRIGHT + Fore.RED + f"The filename '{filename}' already exists in the recent history!")
            elif os.path.exists(filename):
                clearScreen()
                printTitle()
                print(Style.BRIGHT + Fore.RED + "The file already exists!")
            else:
                urls = []
                with open(filename, "w") as file:
                    clearScreen()
                    printTitle()
                    print(Style.BRIGHT + Fore.YELLOW + f"New URL list '{filename}' created successfully!\n")
                    filename = filename
                    break

        # add the new filename to conf/all_files.txt
        all_files_file = "conf/all_files.txt"
        with open(all_files_file, "a") as f:
            f.write(f"{filename}\n")
            print(Style.BRIGHT + Fore.GREEN + f"\n'{filename}' added to the list of available files.\n")



    elif choice == "3":
        clearScreen()
        printTitle()

        # show all URLs
        if not urls:
            clearScreen()
            printTitle()
            print(Style.BRIGHT + Fore.RED + "No URLs found!")
        else:
            print("{:<39}{}".format(Style.BRIGHT + Fore.YELLOW + "Label", "URL\n"))
            for url in urls:
                print("{:<30}{}".format(url[0], url[1]))

            # remove a URL from the list
            label = input(Style.BRIGHT + "\nEnter the label of the URL to remove: ")
            print()
            for url in urls:
                if url[0] == label:  # check if label matches
                    urls.remove(url)
                    clearScreen()
                    printTitle()
                    print(Style.BRIGHT + Fore.GREEN + "URL removed successfully!\n")
                    break
            else:
                clearScreen()
                printTitle()
                print(Style.BRIGHT + Fore.RED + "Label not found!\n")

            # display URLs from file
            file_urls = []
            try:
                with open(filename, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line and ":" in line:
                            label, url = line.split(":", 1)
                            if (label.strip(), url.strip()) not in urls:
                                file_urls.append((label.strip(), url.strip()))
            except FileNotFoundError:
                clearScreen()
                printTitle()
                # display error message if file not found
                print(Style.BRIGHT + Fore.RED + f"{filename} file not found!")


    elif choice == "4":
        clearScreen()
        printTitle()

        # show all URLs
        if not urls:
            clearScreen()
            printTitle()
            print(Style.BRIGHT + Fore.RED + "No URLs found!")
        else:
            print("{:<39}{}".format(Style.BRIGHT + Fore.YELLOW + "Label", "URL\n"))
            for url in urls:
                print("{:<30}{}".format(url[0], url[1]))

            # display URLs from file
            file_urls = []
            try:
                with open(filename, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line and ":" in line:
                            label, url = line.split(":", 1)
                            if (label.strip(), url.strip()) not in urls:
                                file_urls.append((label.strip(), url.strip()))
                        if file_urls:
                            print(Fore.MAGENTA + "\nURLs from file:")
                            for url in file_urls:
                                print("{:<30}{}".format(url[0], url[1]))
            except FileNotFoundError:
                # display error message if file not found
                print(Style.BRIGHT + Fore.RED + "URL List.txt file not found!")

    elif choice == "5":
        clearScreen()
        printTitle()

        print(Style.BRIGHT + Fore.YELLOW + "\nAvailable files:\n")

        # read all filenames from conf/all_files.txt and filter out any that don't exist
        all_files = []
        all_files_file = "conf/all_files.txt"
        if os.path.exists(all_files_file):
            with open(all_files_file, "r") as f:
                for line in f:
                    file_name = line.strip()
                    if os.path.exists(file_name):
                        all_files.append(file_name)
        else:
            open(all_files_file, "w").close()

        # add filenames in the current working directory that are not in the all_files list
        for file_name in os.listdir():
            if file_name.endswith(".txt") and file_name not in all_files:
                all_files.append(file_name)

        for i, file_name in enumerate(all_files):
            print(f"{i+1}. {file_name}")

        while True:
            choice = input(Style.BRIGHT + Fore.YELLOW + "\nEnter the number of the file you want to use: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(all_files):
                    filename = all_files[choice-1]
                    with open("conf/last_filename.txt", "w") as f:
                        f.write(filename)
                    clearScreen()
                    printTitle()
                    print(Style.BRIGHT + Fore.GREEN + f"Successfully changed URL List to {filename}.\n")
                    with open(filename, "r") as file:
                        urls = []
                        for line in file:
                            line = line.strip()
                            if line and ":" in line:
                                label, url = line.split(":", 1)
                                urls.append((label.strip(), url.strip()))
                    break
                else:
                    print(Style.BRIGHT + Fore.RED + "\nInvalid choice! Please enter a number from the list.\n")
            except ValueError:
                print(Style.BRIGHT + Fore.RED + "\nInvalid choice! Please enter a number from the list.\n")

    elif choice == "6":
        clearScreen()
        printTitle()

        # print all .txt files in all_files.txt
        with open("conf/all_files.txt", "r") as f:
            all_files = [line.strip() for line in f.readlines() if line.strip().endswith(".txt")]
            print(Style.BRIGHT + Fore.BLUE + "All .txt files:\n") 
            print(Style.BRIGHT + Fore.RESET + "\n".join(all_files) + "\n")

        # remove a .txt file
        while True:
            filename = input(Style.BRIGHT + "Enter the filename of the file you want to remove (include '.txt' extension): ")
            if not filename.endswith(".txt"):
                print(Style.BRIGHT + Fore.RED + "The filename must end with '.txt'!")
            elif not os.path.exists(filename):
                print(Style.BRIGHT + Fore.RED + f"The file '{filename}' does not exist!")
            else:
                with open("conf/last_filename.txt", "r") as f:
                    last_filename = f.read().strip()
                if filename == last_filename:
                    # select a random file from the list of available files to replace last_filename.txt
                    with open("conf/all_files.txt", "r") as f:
                        all_files = [line.strip() for line in f.readlines() if line.strip().endswith(".txt")]
                    all_files.remove(filename)
                    if all_files:
                        new_last_filename = random.choice(all_files)
                        with open("conf/last_filename.txt", "w") as f:
                            f.write(new_last_filename)
                        print(Style.BRIGHT + Fore.YELLOW + f"'{filename}' was last used. Changing last_filename.txt to '{new_last_filename}'.\n")
                    else:
                        with open("conf/last_filename.txt", "w") as f:
                            f.write("Defult.txt")
                        print(Style.BRIGHT + Fore.RED + f"\n'{filename}' was last used. There are no other available files to set as last_filename.txt.\n")
                confirm = input(Style.BRIGHT + Fore.YELLOW + f"\nAre you sure you want to remove '{filename}'? (y/n): ")
                if confirm.lower() == "y":
                    os.remove(filename)
                    clearScreen()
                    printTitle()
                    print(Style.BRIGHT + Fore.GREEN + f"\n'{filename}' removed successfully!\n")
                    # update the list of available files
                    update_all_files()
                    # if it was the last .txt file, start over
                    if not os.path.exists("conf/all_files.txt"):
                        break
                    with open("conf/all_files.txt", "r") as f:
                        all_files = [line.strip() for line in f.readlines() if line.strip().endswith(".txt")]
                    if not all_files:
                        break
                    if filename == last_filename:
                        # select a random file from the list of available files to replace last_filename.txt
                        filename = random.choice(all_files)
                        with open("conf/last_filename.txt", "w") as f:
                            f.write(filename)
                            print(Style.BRIGHT + Fore.YELLOW + f"'{filename}' is now the last_filename.txt file.\n")
                            filename = new_last_filename
                    break
                else:
                    break



    elif choice == "7":
        clearScreen()
        printTitle()

        # exit the program
        print(Style.BRIGHT + Fore.YELLOW + "\n\nGood Bay...\n\n")
        break

    else:
        clearScreen()
        printTitle()

        # display error message if choice is invalid
        print(Style.BRIGHT + Fore.RED + "Invalid choice!")