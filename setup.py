from setuptools import setup
from ConfigParser import SafeConfigParser
import os, sys
path = '~/.yolog'
path = os.path.expandvars(os.path.expanduser(path))
try:
    os.stat(path)
except:
    os.mkdir(path) 
path = path + '/config.ini'
config = SafeConfigParser()
config.read(path)
config.add_section('main')
config.set('main', 'hash', 'YELLOW')
config.set('main', 'author', 'BLUE')
config.set('main', 'date', 'GREEN')
config.set('main', 'refs', 'RED')
config.set('main', 'description', 'WHITE')
with open(path, 'w') as f:
    config.write(f)
setup(
    name='yolog',
    version='0.2.1',
    description='Beautify your git logs!',
    url='http://github.com/karandesai-96/yolog',
    author='Karan Desai',
    author_email='karandesai281196@gmail.com',
    license='MIT',
    packages=['yolog'],
    entry_points={
        'console_scripts': ['yolog = yolog.main:main']
    },
    zip_safe=True
)
