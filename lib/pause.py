import readchar   # This needs to be installed
import time        
def pause(seconds=None):
    if seconds is None:
        # keyboard.read_key() returns immediately with 'enter'
        # input() requires hitting enter
        readchar.readkey()
    else:
        time.sleep(seconds)        