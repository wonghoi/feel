from os.path import dirname as extract_folder
from sys import executable as python_executable
def pythonroot(): 
    return extract_folder(python_executable)