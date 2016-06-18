from ConfigParser import SafeConfigParser
import os, sys
RESET  = "$(tput sgr0)"
BACKSPACE = "%x08"
config = SafeConfigParser()
path = '~/.yolog/config.ini'
path = os.path.expandvars(os.path.expanduser(path))
config.read(path)
a = config.get('main', 'hash')
b = config.get('main', 'author')
c = config.get('main', 'date')
d = config.get('main', 'refs')
e = config.get('main', 'description')
class YologGenerator(object):
    BLACK  = "$(tput bold)$(tput setaf 0)"
    RED    = "$(tput bold)$(tput setaf 1)"
    GREEN  = "$(tput bold)$(tput setaf 2)"
    YELLOW = "$(tput bold)$(tput setaf 3)"
    BLUE   = "$(tput bold)$(tput setaf 4)"
    PURPLE = "$(tput bold)$(tput setaf 5)"
    CYAN   = "$(tput bold)$(tput setaf 6)"
    WHITE  = "$(tput setaf 7)"
    if (a=='BLACK'):
        a = BLACK
    elif (a=='RED'):
        a = RED
    elif (a=='YELLOW'):
        a = YELLOW
    elif (a=='BLUE'):
        a = BLUE
    elif (a=='PURPLE'):
        a = PURPLE
    elif (a=='CYAN'):
        a = CYAN
    elif (a=='WHITE'):
        a = WHITE
    else:
        a = GREEN
    if (b=='BLACK'):
        b = BLACK
    elif (b=='RED'):
        b = RED
    elif (b=='YELLOW'):
        b = YELLOW
    elif (b=='BLUE'):
        b = BLUE
    elif (b=='PURPLE'):
        b = PURPLE
    elif (b=='CYAN'):
        b = CYAN
    elif (b=='WHITE'):
        b = WHITE
    else:
        b = GREEN
    if (c=='BLACK'):
        c = BLACK
    elif (c=='RED'):
        c = RED
    elif (c=='YELLOW'):
        c = YELLOW
    elif (c=='BLUE'):
        c = BLUE
    elif (c=='PURPLE'):
        c = PURPLE
    elif (c=='CYAN'):
        c = CYAN
    elif (c=='WHITE'):
        c = WHITE
    else:
        c = GREEN
    if (d=='BLACK'):
        d = BLACK
    elif (d=='RED'):
        d = RED
    elif (d=='YELLOW'):
        d = YELLOW
    elif (d=='BLUE'):
        d = BLUE
    elif (d=='PURPLE'):
        d = PURPLE
    elif (d=='CYAN'):
        d = CYAN
    elif (d=='WHITE'):
        d = WHITE
    else:
        d = GREEN
    if (e=='BLACK'):
        e = BLACK
    elif (e=='RED'):
        e = RED
    elif (e=='YELLOW'):
        e = YELLOW
    elif (e=='BLUE'):
        e = BLUE
    elif (e=='PURPLE'):
        e = PURPLE
    elif (e=='CYAN'):
        e = CYAN
    elif (e=='WHITE'):
        e = WHITE
    else:
        e = GREEN                      
    def __init__(self):
        self._hash = "{0}%h{1}".format(self.a, RESET)

        self._author = "{0}%an{1}".format(self.b, RESET)

        self._date = "{0}%aD{1}{2}".format(self.c, BACKSPACE * 15, RESET)

        self._refs = "{0}%d{1}".format(self.d, RESET)

        self._description = "{0}%s{1}".format(self.e, RESET)

        self._format = "{0};;{1};;{2};;{3} {4}".format(
            self._hash, self._author, self._date, self._refs, self._description
        )

    def git_command(self, git_arguments):
        return (
            "git log --pretty=\"tformat:{0}\" --graph --all {1} | "
            "column -t -s \";;\" | less -FXRS".format(
                self._format, git_arguments
            )
        )