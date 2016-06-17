from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')
config.add_section('main')
config.set('main', 'hash', 'YELLOW')
config.set('main', 'author', 'BLUE')
config.set('main', 'date', 'GREEN')
config.set('main', 'refs', 'RED')
config.set('main', 'description', 'WHITE')
with open('config.ini', 'w') as f:
    config.write(f)