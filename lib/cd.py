from glob import escape as escape_pathnames
from os import chdir

def cd(path):
    chdir(escape_pathnames(path))
