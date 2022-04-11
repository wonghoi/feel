import textwrap
def print_dict_item(item, N_key=20, N_val=70, separator_str=' : ', shortener=None):
    key = item[0]
    val = item[1]
    
    lhs = key
    N_lhs = N_key
    if( len(key)>N_key and shortener is not None):
        N_lhs = N_lhs - len(shortener)
        lhs = textwrap.shorten(lhs, width=N_lhs, placeholder=shortener)        
    lhs = lhs.rjust(N_lhs)
    
    sep = separator_str
    
    rhs = val
    N_rhs_indent = N_key+len(sep)
    rhs_indent   = ' '*N_rhs_indent
    if( len(val)>N_val ):
        if shortener is None:
            rhs = textwrap.fill(rhs, width=N_val, initial_indent=rhs_indent, subsequent_indent=rhs_indent).lstrip()
        else:
            rhs = textwrap.shorten(rhs, width=N_val, placeholder=shortener)
            
    lines = lhs + sep + rhs    
    return lines

def disp_dict(d, **kwargs):
    lines = [print_dict_item(x, **kwargs) for x in d.items()]
    print("\n".join(lines))