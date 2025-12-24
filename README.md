# CryptoHotkey

A lightweight, offline cryptography utility for rapid message encryption. This tool operates entirely locally, requires no internet connection, and is optimized for speed and keyboard-centric usage. It's designed to convert plaintext to ciphertext instantly through a minimal interface, emphasizing efficiency, privacy, and ease of use.

## Features

- **Completely Offline:** No internet connection required. Your data never leaves your machine.
- **Keyboard-Centric:** Summon the app with a global hotkey and encrypt without touching your mouse.
- **Instant Clipboard:** The encrypted output is automatically copied to your clipboard.
- **Lightweight & Fast:** A minimal interface and optimized code ensure near-instant operation.
- **Cross-Platform:** Works on Windows, macOS, and Linux.

## Supported Ciphers

- Caesar Cipher
- Base64
- Vigenere Cipher
- Morse Code
- Reverse
- ROTX Cipher
- Bifid Cipher

## Getting Started (For Users)

The easiest way to get started is to download the latest pre-built application for your operating system.

1.  Go to the **[Releases](https://github.com/your-username/your-repository/releases)** page of this repository.
2.  Under the latest release, download the executable file for your system (e.g., `CryptoHotkey.exe` for Windows, `CryptoHotkey` for macOS/Linux).
3.  Run the application. It will run in the background.

## How to Use

1.  Launch the CryptoHotkey application. It will run silently in the system tray or as a background process.
2.  Press `Alt+Ctrl+C` anywhere on your system to open the encryption window.
3.  Use the dropdown to select your desired cipher.
4.  If the cipher requires a key, an input box will appear. Enter the key.
5.  Type or paste your text into the main text area.
6.  Press `Enter`. The window will close, and the ciphertext will be automatically copied to your clipboard.

---

## For Developers

### Running from Source

If you want to run the application from the source code:

1.  **Prerequisites:** Ensure you have Python 3 installed.
2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    python hotkey.py
    ```
    The hotkey listener will now be active.

### Creating a Cross-Platform Release

To package this application into a single, distributable executable for Windows, macOS, and Linux, you can use `PyInstaller`.

**Important:** To create a `.exe` for Windows, you must run PyInstaller on a Windows machine. To create a `.app` for macOS, you must run it on a Mac, and so on for Linux.

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Build the Executable:**
    Navigate to the project's root directory in your terminal and run the following command:

    ```bash
    pyinstaller --onefile --windowed --name CryptoHotkey hotkey.py
    ```
    - `--onefile`: Bundles everything into a single executable file.
    - `--windowed`: Prevents a console window from opening when the application runs.
    - `--name CryptoHotkey`: Sets the name of your final executable.

    The final executable will be located in the `dist/` directory that PyInstaller creates.

3.  **Publishing to GitHub:**
    1.  Go to your repository on GitHub and click on the **"Releases"** tab on the right-hand side.
    2.  Click **"Draft a new release"**.
    3.  Give your release a version number (e.g., `v1.0.0`) and a title.
    4.  In the "Describe this release" section, you can add release notes.
    5.  In the **"Attach binaries"** box, drag and drop the executables you built for each operating system (e.g., `CryptoHotkey.exe`, `CryptoHotkey.app`).
    6.  Click **"Publish release"**.

Now, users can easily download and run your application on different platforms.
