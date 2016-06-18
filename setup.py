from setuptools import setup
from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read('~/.yolog/config.ini')
config.add_section('main')
config.set('main', 'hash', 'YELLOW')
config.set('main', 'author', 'BLUE')
config.set('main', 'date', 'GREEN')
config.set('main', 'refs', 'RED')
config.set('main', 'description', 'WHITE')
with open('~/.yolog/config.ini', 'w') as f:
    config.write(f)
setup(
    name='yolog2',
    version='0.2.1',
    description='Beautify your git logs!',
    url='http://github.com/mangalutsav/yolog',
    author='Karan Desai',
    author_email='karandesai281196@gmail.com',
    license='MIT',
    packages=['yolog'],
    entry_points={
        'console_scripts': ['yolog = yolog.main:main']
    },
    zip_safe=True
)
