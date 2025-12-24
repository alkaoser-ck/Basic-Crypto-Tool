import keyboard
import pyperclip
import queue
import sys
from main import compute

# A queue for thread-safe communication from the hotkey thread to the main thread
gui_queue = queue.Queue()

def request_gui():
    """
    This callback is executed by the keyboard library in a separate thread.
    It puts a message on the queue to request that the GUI be shown.
    """
    gui_queue.put(True)

def main():
    """
    The main function of the application.
    - Sets up the hotkey listener in the background.
    - Runs a loop in the main thread to wait for GUI requests from the hotkey.
    """
    print("Starting Crypto Hotkey listener...")
    print("Press Alt+Ctrl+C to open the encryption window.")
    print("Press Ctrl+C in this terminal to exit if running from source.")

    try:
        # keyboard.add_hotkey starts a background thread listener automatically
        keyboard.add_hotkey("alt+ctrl+c", request_gui)

        # This loop runs in the main thread
        while True:
            # gui_queue.get() is a blocking call that will wait until an item is available
            gui_request = gui_queue.get()

            if gui_request:
                try:
                    # compute() creates the GUI. It's now safely called from the main thread.
                    output = compute()
                    if output is not None:
                        pyperclip.copy(output)
                        print(f"Copied to clipboard: {output}")
                except Exception as e:
                    print(f"Error during GUI operation: {e}", file=sys.stderr)

    except KeyboardInterrupt:
        print("\nShutting down hotkey listener.")
    except Exception as e:
        print(f"A critical error occurred: {e}", file=sys.stderr)
    finally:
        # Clean up all hotkeys
        keyboard.remove_all_hotkeys()

if __name__ == "__main__":
    main()
