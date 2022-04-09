from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Feel (Macros) for various environment'
LONG_DESCRIPTION = 'Syntactic sugar to make other programming language users (such as MATLAB) feel at home with Python'

# Run build_requirements.cmd first to make sure requirements.txt is updated
try:
    with open('requirements.txt') as file: 
        reqs = [line.rstrip() for line in file]
except:
    reqs = []

# Setting up
setup(
        name="feel", 
        version=VERSION,
        author="Hoi Wong",
        author_email="<wonghoi+github@humgar.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=reqs, 
        
        keywords=['matlab', 'macro', 'syntactic sugar', 'feel'],
        classifiers= [
            "Development Status :: 1 - Planning",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
        ]
)