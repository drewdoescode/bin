#''' this is the colors thingy!'''

red = '\033[0;31m'
yellow = '\033[0;33m'
reset = '\033[0m'
clear = '\033[H\033[2J'
blue = '\033[0;34m'
magenta = '\033[0;35m'
violet = '\033[1;35m'
cyan = '\033[0;36m'
green = '\033[0;32m'
base03 = '\033[1;32m'
base02 = '\033[0;30m'
base01 = '\033[1;32m'
base00 = '\033[1;33m'
base0 = '\033[1;34m'
base1 = '\033[1;36m'
base2 = '\033[0;37m'
base3 = '\033[1;37m'
clear = '\033[H\033[2J'
orange = '\033[1;31m'


colors = [clear,red,yellow,reset,clear,blue,magenta,violet,cyan,green,base03,
base02,base01,base00,base0,base1,base2,base1,orange]
def random():
    color = r.choice(colors)
    return color
if __name__ == '__main__':
    print(clear)
    for color in colors:
        print(color + '                       GO BLOCK MCMCMCMCMCMCMCMCMCMCMCMCMC                 ' + reset)
        

