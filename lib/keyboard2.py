from .dbstack import dbstack
# Usage: code.interact(local=locals())   
from code import interact as interactive_session

# Access caller variables
# https://stackoverflow.com/questions/6618795/get-locals-from-calling-namespace-in-python
def get_caller_locals():
    # This function itself added 1 layer already
    # So needs to go 2 layers up to get to the intended caller
    frame = dbstack().f_back.f_back       
    # This might be called at root workspace (no caller)
    return {} if (frame is None) else (frame.f_locals)

# Note that this is an extra stack layer when debugging with this shortcut
# interactive_session does not have this extra stack layer
def keyboard2():
    interactive_session(local=get_caller_locals())        