try:
    import requests
    import os
    import time
    from datetime import datetime
    from colorama import Fore, Style, init
except ImportError:
    print(f"[!] Install the required libraries using the following command: pip install -r requirements.txt")
    exit()

init(autoreset=True)

AVAILABLE = 0
TAKEN = 0

def banner(config):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_text = r"""
   ______           __                     ____             ___
  / ____/___ ______/ /_  ____ _____ ____  / __ )____ _____ <  /
 / / __/ __ `/ ___/ __ \/ __ `/ __ `/ _ \/ __  / __ `/ __ `/ / 
/ /_/ / /_/ / /  / /_/ / /_/ / /_/ /  __/ /_/ / /_/ / /_/ / /  
\____/\__,_/_/  /_.___/\__,_/\__, /\___/_____/\__,_/\__, /_/   
                            /____/                 /____/      

                  GitHub: Schizoverse
"""
    print(Fore.CYAN + banner_text + Style.RESET_ALL if config["color"] == "1" else banner_text)

def timestamp():
    return datetime.now().strftime("%d-%m-%Y")

def load_config(path="config.txt"):
    default = {"color": "1", "logs": "1", "results": "1", "delay": "1000"}
    if not os.path.exists(path):
        with open(path, 'w') as f:
            for k, v in default.items():
                f.write(f"{k} {v}\n")
        return default
    config = {}
    with open(path, 'r') as f:
        for line in f:
            if line.strip() and " " in line:
                k, v = line.strip().split(None, 1)
                config[k] = v
    return config

def load_usernames(file, config):
    if not os.path.exists(file):
        with open(file, 'w'): pass
        text = "[!] 'usernames.txt' created. Add usernames inside."
        print(Fore.YELLOW + text if config["color"] == "1" else text) 
        return []
    with open(file, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def save_result(text, folder="results"):
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/Valid-{timestamp()}.txt", 'a') as f:
        f.write(text + '\n')

def save_log(text, folder="logs"):
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/Log-{timestamp()}.txt", 'a') as f:
        f.write(text + '\n')

def check_username(username, config):
    global AVAILABLE
    global TAKEN

    url = f"https://fragment.com/username/{username.lower()}"
    try:
        r = requests.get(url, allow_redirects=False, timeout=5)
        if r.status_code == 302:
            text = f"[+] {username} - available"
            text2 = " (possibly invalid)"
            print(Fore.GREEN + text + Fore.CYAN + text2 if config["color"] == "1" else text + text2)
            if config["results"] == "1": save_result(username)
            AVAILABLE += 1
        else:
            text = f"[-] {username} - taken"
            print(Fore.RED + text if config["color"] == "1" else text)
            TAKEN += 1
        if config["logs"] == "1":save_log(text)
    except Exception as e:
        err = f"[!] {username} - error:\n> {e}"
        print(Fore.MAGENTA + err if config["color"] == "1" else err)
        if config["logs"] == "1":
            save_log(err)

def main():
    global AVAILABLE
    global TAKEN
    config = load_config()
    banner(config)
    usernames = load_usernames("usernames.txt", config)
    if not usernames:
        name = input("[?] Enter one username to check:\n[>] ").strip()
        if name:
            check_username(name, config)
            text = "\n[#] Finished."
            text2 = f" (saved to Valid-{timestamp()}.txt)"    
            
            if AVAILABLE == 1 and config["results"] == "1":
                print(Fore.WHITE + text + Fore.CYAN + text2 if config["color"] == "1" else text + text2)
            else:
                print(Fore.WHITE + text if config["color"] == "1" else text)
        else:
            text = "[~] Nothing entered."
            print(Fore.MAGENTA + text if config["color"] == "1" else text)
        return
    text = f"[#] Starting.."
    text2 = f" (found {len(usernames)} usernames)\n"
    print(Fore.WHITE + text + Fore.CYAN + text2 if config["color"] == "1" else text + text2)
    delay = int(config.get("delay", "1000")) / 1000
    for username in usernames:
        try:
            check_username(username, config)
        except:
            pass
        time.sleep(delay)
    text = "\n[#] Finished.\n[#] Results: "
    text2 = f"{AVAILABLE}"
    text3 = " | "
    text4 = f"{TAKEN}"
    text5 = f" (available usernames saved to Valid-{timestamp()}.txt)"
    if config["results"] == "1" and AVAILABLE > 0:
        print(Fore.WHITE + text + Fore.GREEN + text2 + Fore.WHITE + text3 + Fore.RED + text4 + Fore.CYAN + text5 if config["color"] == "1" else text + text2 + text3 + text4 + text5)
    else:
        print(Fore.WHITE + text + Fore.GREEN + text2 + Fore.WHITE + text3 + Fore.RED + text4 if config["color"] == "1" else text + text2 + text3 + text4)



if __name__ == "__main__":
    main()
