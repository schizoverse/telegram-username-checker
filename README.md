# Telegram Username Checker
A simple script to check the availability of Telegram usernames without Userbot

## 🚀 Features
- Checks if a Telegram username is **available** or **taken**
- Colored console output (optional)
- Saves logs and results (optional)
- Delay between checks is configurable
- Configurable settings via config.txt
- Fast and lightweight
- Written in Python
- No need to Telegram API or authentication

## 📦 Requirements
- Python 3.7+
- `requests` library
- `colorama` library

Install required libraries with:
```bash
pip install -r requirements.txt
```

## ⚙ How to use
1. Clone the repositry:
```bash
git clone https://github.com/schizoverse/telegram-username-checker.git
```
```bash
cd telegram-username-checker
```
2. Run the script using either:
- `run.bat`
- or `python main.py`
3. The script will automactically:
- Create `usernames.txt` and `config.txt` if they don't exists
- If `usernames.txt` is empty, it will ask for a one username and check it.
## 📝 Configuration
- **`1` = Enable / `0` = Disable**
- `color 1` - enable colored console logs
- `logs 1` - enable saving logs to `./logs/` folder.
- `results 1` - enable saving available username to `./results/` folder
- `delay 1000` - delay beetwen checks in milliseconds
## 📃 usernames.txt
This file contains the list of usernames to check.
Write one username per line like this:
```
username
durov
telegram
```
## 📂 Output
Example output:
```
[+] username1 - available
[-] username2 - taken
```
- Available usernames are saved to:
`./results/Valid-[timestamp].txt`
- Logs are saved to:
`./logs/Log-[timestamp].txt` 
## 🛡️ License
The project is licensed under the **MIT License** - see the [LICENSE](./LICENSE)
> You are free to use, modify, and distribute this software.
> **I'm not responsible** for anything that happens as a result of using it. Use at your own risk. 😎

## 👤 Author
Made with 💻 by [Schizo](https://github.com/schizoverse)
Feel free to fork, contribute, or star the project!

## ☕ Buy me A Coffee (Toncoin)
If you found this useful and want to support the project, feel free to send a little toncoin:
```
UQANkf04uqTZ6o2pRO83sCYpxGFyx7opT9Tcp5CRJ1NZ1NO
```

> **⚠ Note: A username can be "available" on fragment.com but still invalid in Telegram - such cases will be marked as: `[+] username - available (possibly invalid)`**
