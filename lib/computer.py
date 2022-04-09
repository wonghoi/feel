# don't expect the same names as MATLAB
import platform
import sysconfig
import sys
# sys.platform is not very informative since it shows 'win32' for 64-bit Windows

def computer(req=None):
    if req is None:
        # like 'win-amd64'
        return sysconfig.get_platform()
    req = req.lower()
    if req == 'os':
        # like 'windows', 'linux', 'darwin', 'java'
        return platform.machine()
    if req == 'arch':
        # like 'amd64'
        return platform.system()
    if req in ['bits', 'bits_interpreter', 'bits_python']:
        # +1 to account for sign bit
        return sys.maxsize.bit_count()+1
        # This is Python interpreter's bitsize, not the OS though
    if req == 'bits_os':
        # https://docs.python.org/3/library/platform.html#cross-platform
        # platform.architecture output like ('64bit', 'WindowsPE')
        return int(platform.architecture()[0].replace('bit', ''))
