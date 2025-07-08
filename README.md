
# Windows Keylogger

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A Python-based keylogger for Windows, designed for **educational purposes only**. This project demonstrates how to capture and log keyboard inputs using the `pynput` library, serving as a learning tool for understanding system-level input handling and cybersecurity concepts.

⚠️ **DISCLAIMER**: This project is strictly for educational and research purposes. Unauthorized use of keyloggers to capture sensitive information without consent is **illegal** and **unethical**. The author is not responsible for any misuse, damage, or legal consequences caused by this software. Use at your own risk.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

---

## Overview

The Windows Keylogger is a lightweight Python application that captures keyboard inputs on a Windows system and logs them to a file with timestamps. It is intended for educational purposes to help developers and students explore keyboard event handling and logging mechanisms in Python. The keylogger uses the `pynput` library to monitor keystrokes and supports both regular and special keys.

**Note**: This is a proof-of-concept and should only be used in controlled, ethical environments (e.g., on your own machine for learning purposes).

---

## Features

- Captures all keyboard inputs, including alphanumeric and special keys (e.g., Enter, Space, Backspace).
- Logs keystrokes with timestamps to a file (`logfile.txt`).
- Simple and modular code structure for educational clarity.
- Uses the `pynput` library for reliable keyboard event handling.
- Windows-compatible (tested on Windows 10 and 11).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BOOGEY-M4N/windows-keylogger.git
   cd windows-keylogger
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install pynput
   ```

4. Run the keylogger:
   ```bash
   Key logger.py
   ```

---

## Usage

1. After installation, run the keylogger script:
   ```bash
   Key logger.py
   ```

2. The keylogger will start capturing keystrokes and saving them to `logfile.txt` in the project directory and every 5 minutes it will print a timestamp.

3. To stop the keylogger you can use `Ctrl+C` in the terminal. But the `.exe` file will not stop unless you use task manager to "End Task".

4. Check the `logfile.txt` file for the recorded keystrokes.

**Example Output in `logfile.txt`:**
```
##################### Key Logging Started : Tue Jul  8 14:10:21 2025 ##################### 

hello world[Key.enter]
this is a test [Key.enter]
[Key.shift]Hope you enjoy[Key.ctrl]
```

---

## Project Structure

```
windows-keylogger/
│
├── Boogey Man.exe         # Executable keylogger file
├── Key logger.py          # Main keylogger script
├── logfile.txt            # Output file for logged keystrokes
└── README.md              # Project documentation
```

---

## Dependencies

The project requires the following:
- Python 3.8 or higher
- `pynput` (>=1.7.6): For capturing keyboard inputs

Install dependencies using:
```bash
pip install pynput
```

---

## Disclaimer

⚠️ **DANGER**: This software is provided for **educational purposes only**. The author does not endorse or encourage any unauthorized or malicious use of this tool. Keyloggers can be used to harm individuals or systems if misused, and such actions may violate local, national, or international laws. By using this software, you agree that:

- You will only use it in ethical, controlled environments with explicit consent.
- You are solely responsible for any consequences arising from its use.
- The author is not liable for any damages, legal issues, or harm caused by this software.

**Use responsibly and ethically.**

---

## Contact

For questions or feedback, feel free to open an issue on the [GitHub repository](https://github.com/BOOGEY-M4N/windows-keylogger) or contact me via GitHub.

Thank you for exploring this project responsibly!
