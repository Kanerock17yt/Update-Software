import os
import time
import random

# Functions
def start_text():
    print("Thanks for choosing updateSoftware!")
    print("Now it is going to start updating.")
    
    time.sleep(random.randint(1, 2))
    input("Press Enter to start updating.")
    time.sleep(random.randint(1, 3))
    os.system('cls' if os.name == 'nt' else 'clear')

    def print_getingFiles():
        print("Please wait. Getting files.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please wait. Getting files..")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please wait. Getting files...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please wait. Getting files.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please wait. Getting files..")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please wait. Getting files...")

        time.sleep(1)        
        print("Got files.")
        time.sleep(2)
    
    print_getingFiles()
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    


def update_software():
    print("Updating.")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Updating..")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Updating...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Updating.")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Updating..")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Updating...")

    
    print("Preparing to finish update.")
    print("May take 5 seconds.")
    time.sleep(random.randint(1, 5))
    os.system('cls' if os.name == 'nt' else 'clear')



# Code
start_text()

os.system('cls' if os.name == 'nt' else 'clear')

update_software()

time.sleep(random.randint(1, 3))
os.system('cls' if os.name == 'nt' else 'clear')

print("Updated software successfully!")

input("Press Enter to exit.")
