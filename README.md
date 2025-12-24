# CryptoHotkey (Linux Edition)

A lightweight, offline cryptography utility for rapid message encryption. This tool operates entirely locally, requires no internet connection, and is optimized for speed and keyboard-centric usage. It's designed to convert plaintext to ciphertext instantly through a minimal interface, emphasizing efficiency, privacy, and ease of use.

## Features

- **Completely Offline:** No internet connection required. Your data never leaves your machine.
- **Keyboard-Centric:** Summon the app with a global hotkey (`Alt+Ctrl+C`).
- **Instant Clipboard:** The encrypted output is automatically copied to your clipboard.
- **Lightweight & Fast:** A minimal interface and optimized code ensure near-instant operation.

## Supported Ciphers

- Caesar Cipher
- Base64
- Vigenere Cipher
- Morse Code
- Reverse
- ROTX Cipher
- Bifid Cipher

## How to Use

1.  Launch the CryptoHotkey application using the installation guide below. It will run silently in the background.
2.  Press `Alt+Ctrl+C` anywhere on your system to open the encryption window. (The order of modifier keys does not matter).
3.  Use the dropdown to select your desired cipher.
4.  If the cipher requires a key, an input box will appear. Enter the key.
5.  Type or paste your text into the main text area.
6.  Press `Enter`. The window will close, and the ciphertext will be automatically copied to your clipboard.

## Linux Installation Guide

On Linux, the `keyboard` library requires root permissions to function as a global hotkey. The following one-time setup will build the application from source and install it as a system service that runs automatically on startup.

#### Step 1: Install System Dependencies

Choose the command that matches your distribution. These packages are required for the GUI, hotkey, and clipboard functionality.

*   **For Arch-based distributions (e.g., Arch, Manjaro):**
    ```bash
    sudo pacman -S tk xclip
    ```

*   **For Debian-based distributions (e.g., Ubuntu, Mint, Debian):**
    ```bash
    sudo apt update && sudo apt install -y python3-tk xclip
    ```

#### Step 2: Clone Repository and Install Python Packages

This will download the source code and install the necessary Python libraries.
```bash
git clone https://github.com/alkaoser-ck/Basic-Crypto-Tool.git
cd Basic-Crypto-Tool
pip install -r requirements.txt
```

#### Step 3: Build the Executable

This command bundles the entire Python application into a single executable file.
```bash
# Navigate into the 'src' directory where the scripts are
cd src

# Run the build command
pyinstaller --onefile --windowed --name CryptoHotkey --collect-all keyboard --collect-all customtkinter hotkey.py
```

#### Step 4: Install as a System Service

This process moves the application to a standard directory and creates a service file so it starts automatically every time you log in.

1.  **Move the executable:**
    ```bash
    sudo mv dist/CryptoHotkey /usr/local/bin/
    ```

2.  **Create the `systemd` service file:**
    Run `sudo nano /etc/systemd/system/cryptohotkey.service` to create and edit the service file. Paste the following content into the editor.

    **Important:** In the file below, replace `your-username` with your actual Linux username.
    ```ini
    [Unit]
    Description=CryptoHotkey background service
    After=graphical.target

    [Service]
    ExecStart=/usr/local/bin/CryptoHotkey
    Restart=always
    User=your-username
    Environment=DISPLAY=:0
    Environment=XAUTHORITY=/home/your-username/.Xauthority

    [Install]
    WantedBy=graphical.target
    ```
    Save the file and exit the editor (in `nano`, press `Ctrl+X`, then `Y`, then `Enter`).

3.  **Enable and start the service:**
    These commands register the service, enable it to start on boot, and start it for the current session.
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable cryptohotkey.service
    sudo systemctl start cryptohotkey.service
    ```

The setup is now complete! CryptoHotkey will run automatically every time you start your computer. You can use the `Alt+Ctrl+C` hotkey at any time without any further commands.
