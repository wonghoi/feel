# list folders recursively
from glob import glob
from glob import escape
def rdir(p):        
    return glob(escape(p)+'/**/', recursive=True);

# Not faster than glob
#import os    
#def rdir_os(p):
#    return os.popen('''dir/b/s ''' + p).read().splitlines()