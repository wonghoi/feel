import sys

from importlib import reload as reload_module
# Reload (universal in both modes):
def reload_feel():
    # importlib.reload(sys.modules['feel.matlab']) will not reload the libraries
    for mod_name in [x for x in sys.modules.keys() if 'feel.' in x]:
        try:
            reload_module(sys.modules[mod_name])
        except:
            pass