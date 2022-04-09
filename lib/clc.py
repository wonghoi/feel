from .computer import computer
from .system import system
def clc():       
    # 'Linux', 'Darwin', 'Java', 'Windows'
    os_type = computer("os").lower    
    if os_type == 'windows':
        system('cls')
        return
    if os_type == 'linux':
        system('clear')
        return
    print("\033c", end="")       
    
