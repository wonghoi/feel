Macros for shorcuts that make Python feel like MATLAB
=====================================================
Over the years, The Mathworks (TMW) has crystalized their 
Rapid Application Development (RAD) know-hows 
(i.e. experiences over common use cases) to help them design
their language to make users a lot more productive 
provided that they know what is already available. 

Python has a different philosophy so they think protecting 
namespace from pollution comes ahead of coding convneience.

Python does have a valid point guarding the namespace. 
I wasted no time when developing in MATLAB but once in a blue 
moon a coworker shadowed a factory-shipped function, it's
a few wasted days debugging, researching non-invasive workarounds, 
and ending up biting the bullet to find all instances 
of the offending code in a large code base and change it
because most people aren't aware of `addpath(.., '-end')`,
so if I leave it there, the shadowing will haunt unsuspecting noobs.

Situations like this is like less than 0.001% of my dev time.
I'm not sacrificing 99%+ of convenience just to tip-toe around
the design philosophy of Python. This macro is the compromise
that I'm willing to make.

This is made primarily for my own convenience, casually 
updated as I run into more frustrating Python UX issues.
I just find it quicker to write the adapter code than
writing long blog posts covering dozens of observations
that can be expressed in one-liner code

Behavior and the names are expected to change from
version to version until I release a stable version.

Use it at your own risk. I'd suggest reading the comments,
function names and and learn the techniques instead of 
taking it as a serious reference package. It's great
if you are in the Python interpreter (prompt) poking around 
and don't want to be bothered to look up the full path or 
implement helper functions each time to do the basic things 
that's normally done in one-line of MATLAB.

If you have suggestions or features you want to add,
please feel free to raise the issue at Github or just
reach me at <wonghoi+github@humgar.com>

### Usage example: 

####  (most natural)
```
      from feel_matlab import *
      pwd()
```	  
      
####  (preserves namespace) [Recommended]
```
      import feel_matlab as tmw
      tmw.pwd()
```	  
      
Run reload_feel_matlab() after making changes to this macro

Caveats:
- `path` is like MATLAB since it's a member variable
- `cd()/pwd()`, etc need to be called with parentheses as they are functions
  Like C, function names without parenthesis are functors in Python. 
  MATLAB uses `@myfunc`  to refer to functions so calling no args doesn't need `()`