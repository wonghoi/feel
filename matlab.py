'''
Macros for shorcuts that make Python feel like MATLAB
=====================================================
Usage example: 

  (most natural)
      from feel.matlab import *
      pwd()
      
  (preserves namespace) [Recommended]  
      import feel.matlab as tmw
      or
      from feel import matlab as tmw
      
      tmw.pwd()
      
Run reload_feel() after making changes to this macro

Caveats:
- path is like MATLAB since it's a member variable
- cd()/pwd(), etc needs to be called with parenthesis as it's a function
  Like C, function names without parenthesis are functors in Python. 
  MATLAB uses @myfunc  to refer to functions so calling no args doesn't need ()     
'''      
### Self-management
from .lib.reload_feel import reload_feel                
from .lib.reload_all import reload_all        

### Platforms and envrionments
from .lib.computer import computer
from .lib.ver_os import ver_os
from .lib.system import system

### User experience
from .lib.clc import clc   # Use Ctrl+L instead unless you need it programmatically
from .lib.pause import pause

### Inspection
disp = print
from .lib.disp_dict import disp_dict
from .lib.disp_dict import disp_dict_fullview
string = repr   
isprop = hasattr  
from .lib.list_attrib import list_attrib
from .lib.list_functions import list_functions        
from .lib.methods import methods

### Lists
from .lib.unpack_and_stack_lists import unpack_and_stack_lists

### Path manipulation
# MATLAB's cd without input shows as pwd, not used here
from glob import escape as escape_pathnames
from os import chdir
from .lib.cd import cd
from os import mkdir as md
from os import mkdir
from os import getcwd as pwd
from os import listdir as ls
from .lib.rdir import rdir

# python_executable, extract_folder, python_executable
from .lib.pythonroot import *
# fileparts, path2folder_tail, path2head_ext
from .lib.fileparts import *
from os.path import join as fullfile
from os.path import exists as exist_file_or_dir
# addpath, PATH 
from .lib.addpath import *

# MATLAB is exist(str, 'dir') or check for type 7
# isdir searches foldername in search path too
# isfolder searches exact specified & current folder    
from os.path import isfile as isfile    
from os.path import isdir as isdir
# dir is reserved in Python to show attributes
isfolder = exist_dir = isdir

### Resource management
from .lib.onCleanup import onCleanup

### Debugging      
from .lib.dbstack import dbstack
# Exit debugging: Ctrl+D
# dbcont -> (c)ontinue
# dbquit -> (r)eturn or Ctrl+D
# ipdb needs to be downloaded
# https://hasil-sharma.github.io/2017-05-13-python-ipdb/
from ipdb import set_trace as keyboard
# Alternative method using code package's interactive interpreter
# (pass locals() workspace down to the new session)
from .lib.keyboard2 import keyboard2
 
# Pretty print display hook turned on by default 
from .lib.customize import displayhooks                                
                
### Stuff to execute
#print("Feel MATLAB macros executed.")