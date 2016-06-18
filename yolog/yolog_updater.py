from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('~/.yolog/config.ini')

class YologUpdater( arg )
	if arg[0] != 'author' and arg[0] != 'hash' and arg[0] != 'description' and arg[0] != 'date' and args[0] != 'refs'
		return '-1'
	elif arg[1] != 'WHITE' and arg[1] != 'BLACK' and arg[1] != 'RED' and arg[1] != 'GREEN' and arg[1] != 'CYAN' and arg[1] != 'BLUE' and arg[1] != 'PURPLE'
		return '-2'
	else 
		config.set('main',arg[0],arg[1])
		with open('~/.yolog/config.ini', 'w') as f:
    	config.write(f)