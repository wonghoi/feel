import textwrap
def print_dict_item(item, N_key=20, N_val=75, sep=' : ', shortener=None):
    key = item[0]
    val = item[1]
    
    lhs = key.rjust(N_key)
    
    try:
        rhs = str(val)                
    except:
        try:
            rhs = type(val)
        except:
            raise TypeError("Type cannot be cased into string for display")
        
    N_rhs_indent = N_key+len(sep)
    rhs_indent   = ' '*N_rhs_indent
    if( len(rhs)>N_val ):
        if shortener is None:
            rhs = textwrap.fill(rhs, width=N_val, initial_indent=rhs_indent, subsequent_indent=rhs_indent).lstrip()
        else:
            rhs = textwrap.shorten(rhs, width=N_val, placeholder=shortener)
                
            
    lines = lhs + sep + rhs    
    return lines


def disp_dict_fullview(d):
    n_key = max([len(k)      for k in d.keys()])
    n_val = max([len(str(k)) for k in d.values()])
    lines = [print_dict_item(x, N_key=n_key, N_val=n_val) for x in d.items()]
    print("\n".join(lines))

def disp_dict(d, **kwargs):
    lines = [print_dict_item(x, **kwargs) for x in d.items()]
    print("\n".join(lines))