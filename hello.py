import sys, time

def typewriter(string):
    for letter in string:
        sys.stdout.flush()
        time.sleep(.001)
        print(letter, end="")

typewriter(" _    _    ____    _      _       _____ \n")
typewriter("| |  | |  |  __|  | |    | |     |  _  |\n")
typewriter("| |__| |  | |__   | |    | |     | | | |\n")
typewriter("|  __  |  |  __|  | |    | |     | | | |\n")
typewriter("| |  | |  | |__   | |__  | |__   | |_| |\n")
typewriter("|_|  |_|  |____|  |____| |____|  |_____|\n")
typewriter(" _       _    _____    _____     _       ____     _ \n")
typewriter("| |  _  | |  |  _  |  | |_| |   | |     |  _ \   | |\n")
typewriter("| | | | | |  | | | |  |_____|   | |     | | | |  | |\n")
typewriter("| |_| |_| |  | | | |  | |\ \    | |     | | | |  |_|\n")
typewriter("|    _    |  | |_| |  | | \ \   | |__   | |_| |   _ \n")
typewriter("|___| |___|  |_____|  |_|  \_\  |____|  |____/   |_|\n")
print("\n\n")