from os import path

from utils.param_func import *

__version__ = '1.3.5'

cur_dir = path.dirname(path.dirname(path.abspath(__file__)))

DEBUG   = True

LOG_FILE = path.join(cur_dir, 'logs/runtime_{time:YYYYMMDD}.log') 

consoleLogFormat = '<cyan>fuckCpp</cyan>: <level>{message}</level>'

fileLogFormat    =  "{time:YYYY.MM.DD HH:mm:ss} - {thread.name} | {module}.{function}:{line} - {level}:\n{message}"

helpInfo = '''
Usage: fuckCpp file [options]...
Options:
    -h --help       Display This Help Info
    -v --version    Show FuckCpp build version
    --show-log      Show FuckCpp runtime log directory

    -l <level>      Set confusion level to <level>, default value is 'low'
    -o <file>       Place the output into <file>, default value is 'confused.cpp'
    
    -z --zip        Zip the output source file
    --no-confuse    Ask FuckCpp not to confuse your source
'''

cppExtensionNames = [
    '.cp', '.cpp', '.h', '.hpp', '.c'
]

confuseKeywords = [
    'scanf', 'printf', 'cin', 'cout',
    'putchar', 'puts', 'getchar', 'rand',
    'long long', 'int', 'const', 'char',
    'true', 'false', 'inline', 'struct',
    'bool', '__gcd', 'memset', 'NULL',
    'private', 'public', 'void', 'while',
    'for', 'auto', 'size_t', 'if', 'return',
    'else'
]

# 'src' will be given when handling argv
defaultParamData = {
    'level': 'low',
    'output': 'confused.cpp',
    'zipSrc': False,
    'noConfuse': False
}

sameMeaning = {
    '--zip': '-z',
    '--help': '-h',
    '--version': '-v'
}

paramType = {
    '-h': 'function',
    '-v': 'function',
    '-l': 'data',
    '-o': 'data',
    '-z': 'boolean',
    '--no-confuse': 'boolean',
    '--show-log': 'function'
}

paramName = {
    '-h': 'help',
    '-v': 'version',
    '-l': 'level',
    '-o': 'output',
    '-z': 'zipSrc',
    '--no-confuse': 'noConfuse',
    '--show-log': 'showLog'
}

functionMap = {
    'help': genShowHelp(helpInfo),
    'version': genShowVersion(__version__),
    'showLog': genLogPos(path.join(cur_dir, 'logs'))
}

NodeRunTime = {
    'win32': 'node.exe',
    'linux': 'bin/node',
    'darwin': 'bin/node'
}
