import inspect
def list_functions(x, kind=None):

    if inspect.ismodule(x):
        if kind is None:
            kind = 'all'
        
        kind = kind.lower()
        # class is synomous with instance here
        kind = kind.replace('all', 'routine')
        
        # ismethod does not make sense for modules (return empty)
        # isroutine is everything possible
        # isbuiltin shows any builtin function (such as isprop/os.chdir/os.mkdir, etc.)            
        # isfunction is the same as non-builtins, so
        # isroutine is partitioned by isfunction and isbuiltin
            
        screening = {
            'builtin' : inspect.isbuiltin,
            'routine' : inspect.isroutine,
            'defined' : inspect.isfunction,
        }
        return [x[0] for x in inspect.getmembers(x, predicate=screening[kind])]
    else:    
        raise typeError("list_functions is right now developed for modules. User methods() for c")
        
    