# https://stackoverflow.com/questions/17248383/pretty-print-by-default-in-python-repl
from pprint import pprint as prettyprinter
# __builtins__ only work when you are the root stack, not inside a module
# user builtins module to get direct access to the builtins
import builtins
import sys

from ...lib.disp_dict import disp_dict
import collections

# https://docs.python.org/2/library/sys.html#sys.displayhook
# prints to sys.stdout and save value to __builtin__._
orig_displayhook = sys.displayhook
def displayhook_pprint(value):
    # The hook calls only if there's stuff to read
    if value != None:
        # The last output goes to variable named _ in the root workspace
        builtins._ = value
        # Basically the difference is that this hook intercepts the
        # value and pretty print it instead of directly sending it to stdout
        if isinstance(value, dict):
            disp_dict(value)
        else:
            prettyprinter(value)

builtins.pprint_on  = pprint_on  = lambda: setattr(sys, 'displayhook', displayhook_pprint)
builtins.pprint_off = pprint_off = lambda: setattr(sys, 'displayhook', orig_displayhook)
builtins.reset_displayhook = reset_displaybook = lambda: setattr(sys, 'displayhook', sys.__displayhook__)

def is_pprint_on():
    return sys.displayhook==displayhook_pprint

# Pretty print display hook is on by default
pprint_on()
# print(f"Is pretty print on? {is_pprint_on()}")

