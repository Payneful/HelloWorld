import sys, time, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(string):
    for letter in string:
        sys.stdout.flush()
        time.sleep(.001)
        print(letter, end="")


def main():
    clear()
    typewriter(" _    _    ____    _      _       _____ \n"
               "| |  | |  |  __|  | |    | |     |  _  |\n"
               "| |__| |  | |__   | |    | |     | | | |\n"
               "|  __  |  |  __|  | |    | |     | | | |\n"
               "| |  | |  | |__   | |__  | |__   | |_| |\n"
               "|_|  |_|  |____|  |____| |____|  |_____|\n"
               " _       _    _____    _____     _       ____     _ \n"
               "| |  _  | |  |  _  |  | |_| |   | |     |  _ \   | |\n"
               "| | | | | |  | | | |  |_____|   | |     | | | |  | |\n"
               "| |_| |_| |  | | | |  | |\ \    | |     | | | |  |_|\n"
               "|    _    |  | |_| |  | | \ \   | |__   | |_| |   _ \n"
               "|___| |___|  |_____|  |_|  \_\  |____|  |____/   |_|\n\n\n")
    
if __name__ == "__main__":
    main()