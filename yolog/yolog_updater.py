from ConfigParser import SafeConfigParser
import os, sys
config = SafeConfigParser()
path = '~/.yolog/config.ini'
path = os.path.expandvars(os.path.expanduser(path))
config.read(path)
class YologUpdater(object)	:
	if sys.argv[2] != 'author' and sys.argv[2] != 'hash' and sys.argv[2] != 'description' and sys.argv[2] != 'date' and sys.argvs[2] != 'refs':
		print 'invalid type'
	elif sys.argv[3] != 'WHITE' and sys.argv[3] != 'BLACK' and sys.argv[3] != 'RED' and sys.argv[3] != 'GREEN' and sys.argv[3] != 'CYAN' and sys.argv[3] != 'BLUE' and sys.argv[3] != 'PURPLE':
		print 'invalid color'
	else:
		config.set('main',sys.argv[2],sys.argv[3])
		with open(path, 'w') as f:
			config.write(f)