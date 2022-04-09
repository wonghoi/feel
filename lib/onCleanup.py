# https://wonghoi.humgar.com/blog/2019/05/06/handling-resources-that-needs-to-be-cleaned-up-in-python-and-matlab/
'''
Usage:
    try:
        f = File()
    except:
        print("Cannot open file")
    else:
        cleanup_obj = onCleanup(lambda x = f: x.custom_cleanup())
            
x.custom_cleanup() is just a placeholder for writing cleanup code that
optionally involves x, which is bounded to the file pointer f    

Capturing is mandatory because Python is late-binding by default
while MATLAB is early-binding by default (captured on creation)
'''    
class onCleanup:
    def __init__(self, functor):
        self.task = functor;
    def __del__(self):
        self.task()
