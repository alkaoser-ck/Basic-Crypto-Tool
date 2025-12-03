# Crypto Hotkey

A simple, lightweight desktop utility to quickly encrypt/encode text using various ciphers. Activate the tool anytime with a global hotkey, enter your text, choose your cipher, and the result is automatically copied to your clipboard.

![Screenshot of the Crypto Hotkey application window](https'://i.imgur.com/your-screenshot.png')
*(You can replace the link above with a real screenshot of your application after you create one.)*

## Features

- **Global Hotkey**: Press `Alt+Ctrl+C` from any application to launch the encryption window.
- **Multiple Ciphers**: Supports a variety of ciphers including Caesar, Vigenere, Base64, Morse Code, and more.
- **Clipboard Integration**: The encrypted/encoded output is automatically copied to your clipboard.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## Using the Application (For End-Users)

The easiest way to use Crypto Hotkey is to download the latest pre-built application from the **[Releases](https'://github.com/your-username/your-repo/releases')** page of this repository.

1.  Go to the Releases page.
2.  Download the appropriate executable file for your operating system (e.g., `CryptoHotkey-Windows.exe`, `CryptoHotkey-Linux`, or `CryptoHotkey-macOS`).
3.  Move the downloaded file to a permanent location on your computer (e.g., `C:\Program Files\CryptoHotkey` on Windows or `/opt/CryptoHotkey` on Linux).

### Running on System Startup

For the hotkey to work at all times, the application needs to be running in the background. Here’s how to make it start automatically when you turn on your computer.

#### Windows

1.  Create a shortcut to the `.exe` file you downloaded.
2.  Press `Win + R`, type `shell:startup`, and press Enter. This will open your Startup folder.
3.  Move the shortcut you created into this folder.

The application will now start automatically when you log in.

#### macOS

1.  Open **System Settings** > **General** > **Login Items**.
2.  Under "Open at Login", click the `+` button.
3.  Find and select the `CryptoHotkey-macOS` application you downloaded.

**Note for macOS & Linux**: The first time you run the application, your system may ask for permissions to monitor keyboard input or for accessibility access. You must grant these permissions for the global hotkey to work. You may also need to run the application with `sudo` for the first time or provide permissions in the system settings.

#### Linux

There are two main ways to autostart an application on most Linux desktop environments.

**Method 1: Using a `.desktop` file (Recommended)**

1.  Create a file named `CryptoHotkey.desktop` in `~/.config/autostart/`.
2.  Open the file and add the following content, making sure to replace `/path/to/your/CryptoHotkey-Linux` with the actual path to the executable:

    ```ini
    [Desktop Entry]
    Type=Application
    Name=Crypto Hotkey
    Exec=/path/to/your/CryptoHotkey-Linux
    Comment=A background hotkey tool for text encryption.
    ```
3.  Save the file and make it executable: `chmod +x ~/.config/autostart/CryptoHotkey.desktop`.

**Important**: On Linux, the `keyboard` library requires root permissions to function as a global hotkey. This means you must run the application with `sudo`. To make this work on startup, you may need to configure `sudoers` to allow running the app without a password or modify the `.desktop` file's `Exec` line to something like `Exec=sudo /path/to/your/CryptoHotkey-Linux`. This can be complex and depends on your system's security setup.

---

## For Developers

If you want to run the application from source or build it yourself, follow these instructions.

### Prerequisites

-   Python 3.8+
-   `pip` and `venv`

### Running from Source

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python src/hotkey.py
    ```
    **On Linux**, you will need to run this with `sudo` for the global hotkey to work:
    ```bash
    sudo venv/bin/python src/hotkey.py
    ```

### Building the Executable

This project uses **PyInstaller** to create a single-file executable.

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  **Run the build command:**
    From the root of the project directory, run the following command.

    -   **On Windows/macOS**:
        ```bash
        pyinstaller --name "CryptoHotkey" --onefile --noconsole --icon=path/to/your/icon.ico src/hotkey.py
        ```
    -   **On Linux**:
        ```bash
        pyinstaller --name "CryptoHotkey" --onefile --noconsole src/hotkey.py
        ```
    
    *   `--onefile`: Bundles everything into a single executable.
    *   `--noconsole`: Prevents the terminal/console window from appearing when you run the application.
    *   `--name`: Sets the name of the final executable.
    *   `--icon`: (Optional) You can add a custom icon to your `.exe` file.

3.  The final executable will be located in the `dist/` directory. You can then distribute this file.
