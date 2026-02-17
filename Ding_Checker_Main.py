import os
import time

def clear_screen():
    # Clears the terminal screen based on your OS (Windows or Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def fake_loading():
    print("Verifying Identity...")
    for i in range(1, 11):
        # Creates a progress bar [##########]
        print(f"[{'#' * i}{' ' * (10 - i)}] {i*10}%", end='\r')
        time.sleep(0.1)
    print("\nScan Complete.\n")

def ding_checker():
    while True:
        clear_screen()
        print("--- SECURITY CHECK: PROJECT DING ---")
        
        # .strip().lower() makes " YES " or "Yes" work
        answer = input("Does Ding like piano? ").strip().lower()

        fake_loading()

        if answer == "no":
            print("ACCESS GRANTED: This is Ding.")
            break # Exits the loop
        elif answer == "yes":
            print("!!! SECURITY BREACH !!!")
            print("Buddy you are not Ding GTFO.")
            break 
        else:
            print("Error: Suspect input detected. Retrying...")
            time.sleep(1.5)

if __name__ == "__main__":
    ding_checker()
