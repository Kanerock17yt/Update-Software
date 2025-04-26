import os
import time
import random

# Functions
def start_text():
    print("Thanks for choosing updateSoftware!")
    print("Now it is going to start updating.")
    print("Please wait. Geting files...")
    time.sleep(random.randint(1, 2))
    input("Press Enter to start updating.")

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



# Code
start_text()

os.system('cls' if os.name == 'nt' else 'clear')

update_software()

time.sleep(random.randint(1, 3))
os.system('cls' if os.name == 'nt' else 'clear')

print("Updated software successfully!")

input("Press Enter to exit.")
