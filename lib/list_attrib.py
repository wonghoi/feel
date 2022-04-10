# Dummies
from . import __dummy_module__ as dummy_module

class dummy_class:    
    pass
    
def dummy_function():
    pass

## This gets rid of the the boilerplate attributes
import inspect
def list_attrib(x):
# Do not feed an instance of an object.
# wrap it with type() instead.
    if inspect.ismodule(x):
        dummy = dummy_module
    elif inspect.isclass(x):
        dummy = dummy_class
    elif inspect.isroutine(x):
        dummy = dummy_function
    else:
        raise TypeError(f"{type(x)} unsupported. Call with type(x) if it's an instantiation.")
    
    return list(sorted(set(dir(x))-set(dir(dummy))))