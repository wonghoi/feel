# This is 'methods' in MATLAB / C++ sense, i.e. any member functions
# of the class. Python separates bound/unbound methods which the bound
# ones are called classes and the rest are functions.
#
# i.e. for class C with function f defined, aka 
#
# class C: 
#   def f: pass,
#
# inspect.ismethod( C().a ) -> True
# inspect.isfunction( C().a ) -> False
# inspect.ismethod( C.a ) -> False
# inspect.isfunction( C.a ) -> True
#
# This means you need to 

import inspect
def methods(x, kind=None):
# I don't know functions function to check for object instances (doesn't count as classes) for now
# Trust the user not to abuse it for non-classes for now

#    if inspect.isclass(x):
        if kind is None:
            kind = 'any'
        
        kind = kind.lower()
        # class is synomous with instance here
        kind = kind.replace('class', 'instance')
        # routine covers all possible member functions including unimplemented dunder
        kind = kind.replace('all', 'routine')
        # unimplemented = routine - any, including imports that are not overloaded/redefiend
        # native data types like integers and strings are ALL builtin, so builtin=routine
        screening = {
            'builtin'       : inspect.isbuiltin,
            'routine'       : inspect.isroutine,
            'unimplemented' : lambda x: not inspect.isfunction(x) and not inspect.ismethod(x) and inspect.isroutine(x),
            'implemented'   : lambda x:     inspect.isfunction(x) or      inspect.ismethod(x) or  inspect.isbuiltin(x),
            'dual'          : lambda x:     inspect.isfunction(x) and     inspect.ismethod(x),
            'any'           : lambda x:     inspect.isfunction(x) or      inspect.ismethod(x),
            'static'        :               inspect.isfunction,
            'instance'      :                                             inspect.ismethod,
            'static_pure'   : lambda x:     inspect.isfunction(x) and not inspect.ismethod(x),
            'instance_pure' : lambda x: not inspect.isfunction(x) and     inspect.ismethod(x),
        }
        return [x[0] for x in inspect.getmembers(x, predicate=screening[kind])]
#    else:    
#        raise typeError("methods() makes sense only for classes")
        
    