from sys import exit

def genShowHelp(helpInfo : str):
    def ret():
        print(helpInfo)
        exit(0)
    return ret

def genShowVersion(version : str):
    def ret():
        print('FuckCpp v' + version)
        exit(0)
    return ret