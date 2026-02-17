import os
import time
import sys

def security_terminal():
    # Setup for CMD/Terminal window
    os.system('color 0a' if os.name == 'nt' else '') # Green text for that hacker vibe
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=========================================")
        print("   OFFICIAL DING VERIFICATION SYSTEM    ")
        print("=========================================\n")

        # Question 1
        q1 = input("[Does Ding like piano? ").strip().lower()
        
        # Question 2
        q2 = input("Is Litong good at piano? ").strip().lower()

        print("\n[SYSTEM] Analyzing responses...")
        time.sleep(1.5)

        # Logic Matrix
        if q1 == "no" and q2 == "no":
            print("\nMATCH FOUND: 100% Probability.")
            print("Welcome back, Ding.")
            time.sleep(1) # Dramatic pause
            print("By the way, we both know you like Kaydi.") # Added the requested line
            input("\nPress Enter to exit...")
            break
        elif q1 == "yes" or q2 == "yes":
            print("\nCRITICAL ERROR: Imposter Detected.")
            print("Buddy you are not Ding GTFO.")
            input("\nPress Enter to exit and stay away...")
            sys.exit()
        else:
            print("\nDATA INCONCLUSIVE. Restarting scan...")
            time.sleep(2)

if __name__ == "__main__":
    try:
        security_terminal()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting...")
        sys.exit()
