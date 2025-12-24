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

On Linux, capturing global keyboard events (like a system-wide hotkey) requires elevated permissions. For this reason, this guide will help you install CryptoHotkey as a **systemd service** that runs as `root`. This is a one-time setup that will build the application from source and ensure it starts automatically and reliably every time you boot your computer.

### Step 1: Install System Dependencies

Choose the command that matches your distribution. These packages are required for the GUI, hotkey functionality, and clipboard integration.

*   **For Arch-based distributions (e.g., Arch, Manjaro):**
    ```bash
    sudo pacman -S --noconfirm tk xclip git
    ```

*   **For Debian-based distributions (e.g., Ubuntu, Mint, Debian):**
    ```bash
    sudo apt update && sudo apt install -y python3-tk xclip git
    ```

### Step 2: Clone the Repository and Set Up a Virtual Environment

This will download the source code and create a safe, isolated Python environment for the application's dependencies. This prevents conflicts with system-wide packages.

```bash
# Clone the repository
git clone https://github.com/alkaoser-ck/Basic-Crypto-Tool.git
cd Basic-Crypto-Tool

# Create and activate a Python virtual environment
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies

Now, with the virtual environment active, install the required Python libraries.

```bash
# The command prompt should now be prefixed with (venv)
pip install -r requirements.txt
pip install pyinstaller
```

### Step 4: Run the Application as a System Service

This final step will create a `systemd` service file and start the application. This makes the hotkey available automatically after every reboot.

1.  **Create the Service File:**
    This command will create the `systemd` service file for you. It automatically inserts the correct paths for the Python executable and the script.

    ```bash
    # Create the service file using a here-document
    sudo bash -c "cat > /etc/systemd/system/cryptohotkey.service" <<EOF
    [Unit]
    Description=CryptoHotkey Service
    After=multi-user.target

    [Service]
    User=root
    Group=root
    ExecStart=$(pwd)/venv/bin/python $(pwd)/src/hotkey.py
    Restart=on-failure
    StandardOutput=journal
    StandardError=journal

    [Install]
    WantedBy=multi-user.target
    EOF
    ```

2.  **Enable and Start the Service:**
    This command will reload `systemd`, enable the service to start on boot, and start it immediately.

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable --now cryptohotkey.service
    ```

3.  **(Optional) Check the Service Status:**
    To confirm that the service is running correctly, you can use the following command:

    ```bash
    sudo systemctl status cryptohotkey.service
    ```
    If the service is active and running, you're all set!

The setup is now complete! CryptoHotkey will run automatically and silently in the background every time you start your computer. You can use the `Alt+Ctrl+C` hotkey at any time.
