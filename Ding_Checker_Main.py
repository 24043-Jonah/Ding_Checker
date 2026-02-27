import os
import time
import sys
import shutil
import subprocess
import threading

def self_destruct():
    """Clears the console and ensures no trace is left."""
    if os.path.exists("Ding_Secret_Vault"):
        shutil.rmtree("Ding_Secret_Vault")
    if os.path.exists("SECRET_INSTRUCTIONS.txt"):
        os.remove("SECRET_INSTRUCTIONS.txt")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n[SYSTEM] SELF-DESTRUCT COMPLETE. EVIDENCE PURGED.")
    time.sleep(1)
    os._exit(0)

def wait_for_user_input(stop_event):
    """Listens for the Enter key to trigger manual shred."""
    input()
    stop_event.set()

def security_terminal():
    if os.name == 'nt':
        os.system('title DING VERIFICATION SYSTEM & color 0a')

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌─────────────────────────────────────────┐")
        print("│      OFFICIAL DING VERIFICATION SYSTEM  │")
        print("└─────────────────────────────────────────┘\n")

        q1 = input("[SEC-1] Does Ding like piano? ").strip().lower()
        q2 = input("[SEC-2] Is Litong good at piano? ").strip().lower()
        q3 = input("[SEC-3] Did Virtuoso Strings deserve to win Chamber Nats 2025? ").strip().lower()

        print("\n[SYSTEM] Verifying Credentials...")
        time.sleep(1.2)

        # ACCESS GRANTED logic
        if q1 == "no" and q2 == "no" and q3 == "no":
            print("\nACCESS GRANTED. Welcome, Operator.")
            
            # --- FILE CREATION ---
            file_path = os.path.abspath("SECRET_INSTRUCTIONS.txt")
            with open(file_path, "w") as f:
                f.write("OFFICIAL INSTRUCTIONS:\n\nYou should bash Litong...\nPIN: 0220")

            # --- SMOOTH OPENING (Direct to TXT) ---
            print("[SYSTEM] Opening Secure Document...")
            if os.name == 'nt':
                os.startfile(file_path) # Opens in Notepad/Default Editor

            print("\n" + "!"*45)
            print("!!! WARNING: DATA IS DECRYPTED !!!")
            print("File will auto-shred in 30 seconds.")
            print("Press [ENTER] to shred immediately.")
            print("!"*45)

            # --- COUNTDOWN ---
            stop_event = threading.Event()
            input_thread = threading.Thread(target=wait_for_user_input, args=(stop_event,), daemon=True)
            input_thread.start()

            for i in range(30, 0, -1):
                if stop_event.is_set():
                    break
                sys.stdout.write(f"\rSHREDDING IN: {i:02d}s ")
                sys.stdout.flush()
                time.sleep(1)

            # --- CLEANUP ---
            # Close Notepad if it's open
            if os.name == 'nt':
                subprocess.run(['taskkill', '/FI', 'WINDOWTITLE eq SECRET_INSTRUCTIONS.txt*', '/F'], capture_output=True)
            
            if os.path.exists(file_path):
                os.remove(file_path)
            
            print("\n\n" + "="*45)
            print("[SYSTEM] SESSION TERMINATED: File Shredded.")
            print("="*45)
            time.sleep(1.5)
            break

        else:
            print("\n" + "!"*40)
            print("CRITICAL ERROR: Imposter Detected.")
            print("Initiating counter-measures...")
            print("!"*40)
            time.sleep(2)
            self_destruct()

if __name__ == "__main__":
    try:
        security_terminal()
    except KeyboardInterrupt:
        self_destruct()
