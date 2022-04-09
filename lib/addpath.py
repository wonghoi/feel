from sys import path as PATH

# idiom: addpath(rdir()) is like MATLAB's addpath(genpath())
def addpath(p, to_which_end='bottom'):
    new_p = set(p) - set(PATH)
    
    if to_which_end == 'top':
        PATH = list(new_p) + PATH
    elif to_which_end == 'bottom':
        PATH.extend( new_p )
    else:
        raise f"invalid end for adding path specified: {to_which_end}"
    


    
   
        

