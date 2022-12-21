from sys import argv, exit
from loguru import logger
from random import randint

argc = len(argv)

helpInfo = '''
Usage: fuckCpp.exe [options] file...
Options:
    -h              Display This Help Info
    -l <level>      Set confusion level to <level>
    -o <file>       Place the output into <file>
'''

ZIP_URL = 'https://mivik.gitee.io/compress'

class Config:
    confusionLevel  = 'low'
    fileSrc         = ''
    outputName      = 'confused.cpp'
    zipSrc          = False
    keywords = [
        'scanf', 'printf', 'cin', 'cout',
        'putchar', 'puts', 'getchar', 'rand',
        'long long', 'int', 'const', 'char', 
        'true', 'false', 'inline', 'struct',
        'bool', '__gcd', 'memset', 'NULL',
        'private', 'public', 'void', 'while',
        'for', 'auto', 'size_t', 'if', 'return', 
        'else'
    ]
    @logger.catch
    def isCppFile(name: str) -> bool:
        extensionName = [
            '.cp', '.cpp', '.h', '.hpp', '.c'
        ]
        for matchName in extensionName:
            if name.endswith(matchName):
                return True
        return False

    @logger.catch
    def readConfig() -> None: 
        jump = False
        for i in range(argc):
            if jump:
                jump = False
                continue
            item = argv[i]
            if Config.isCppFile(item):
                Config.fileSrc = item
            if item == '-o':
                jump = True
                Config.outputName = argv[i + 1]
            if item == '-l':
                jump = True
                Config.confusionLevel = argv[i + 1]
            if item == '-h':
                print(helpInfo)
                exit(0)
            if item == '--zip':
                Config.zipSrc = True
        if Config.fileSrc == '':
            logger.critical('No Input File Given')

UsedName = []

@logger.catch
def genRandName() -> str:
    seed = randint(0x100000, 0xffffff)
    while seed in UsedName:
        seed = randint(0x100000, 0xffffff)
    UsedName.append(seed)
    return '_' + hex(seed)

@logger.catch
def isPreProcessLine(line: str) -> bool:
    for char in line:
        if char != ' ': 
            return char == '#'
    return False # Bug: All Space Line

@logger.catch
def getReservedPart(line: str) -> tuple:
    # Returns (reserved, requireChange)
    reserved = ''
    foundSharp = False
    while len(line):
        changeChar = line[0]
        line = line[1:]
        reserved += changeChar
        if changeChar == '#':
            foundSharp = True
        if foundSharp and changeChar == ' ':
            break
    return (reserved, line)

@logger.catch
def zipCpp(src: str) -> str:
    # 整合压行代码
    return src

@logger.catch
def main() -> int:
    # Analyze args
    Config.readConfig()
    keywords   = Config.keywords
    sourceFile = open(Config.fileSrc, 'r', encoding = 'u8')
    outPutFile = open(Config.outputName, 'w', encoding = 'u8')
    keywordMatch = {}
    toWrite = ''
    # Simple Fuck
    for item in keywords:
        keywordMatch[item] = genRandName()
        toWrite += (
            f'#define {keywordMatch[item]} {item}' + '\n'
        )
    for line in sourceFile.readlines():
        line = line.replace('\n', '')
        # print(line)
        reserved = ''
        if isPreProcessLine(line):
            reserved, line = getReservedPart(line)
        for replace in keywords:
            line = line.replace(replace, keywordMatch[replace])
        toWrite += (reserved + line + '\n')
    if Config.zipSrc:
        toWrite = zipCpp(toWrite)
    outPutFile.write(toWrite)
    return 0

if __name__ == '__main__':
    exit(main())