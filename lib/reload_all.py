import sys

### https://www.oreilly.com/library/view/python-cookbook/0596001673/ch14s02.html        
def reload_all():
    if 'init_modules' in globals():
        # second or subsequent run: remove all but initially loaded modules
        for m in sys.modules.keys():
            if m not in init_modules:
                del(sys.modules[m])
    else:
        # first run: find out which modules were initially loaded
        init_modules = sys.modules.keys(  )