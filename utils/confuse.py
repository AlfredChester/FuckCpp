from json import dumps
from utils.logger import *
from random import randint

@logger.catch
class confuser:
    @logger.catch
    def isPreProcessLine(self, line: str) -> bool:
        for char in line:
            if char != ' ': 
                return char == '#'
        return False

    @logger.catch
    def getReservedPart(self, line: str) -> tuple:
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
    def genRandName(self) -> str:
        seed = randint(0x100000, 0xffffff)
        while seed in self.UsedName:
            seed = randint(0x100000, 0xffffff)
        self.UsedName.append(seed)
        return '_' + hex(seed)

    @logger.catch
    def genConfused(self, text) -> str:
        toWrite = ''
        for item in self.keywords:
            toWrite += f'#define {self.keywordMatch[item]} {item}\n'
        for line in text:
            line = line.replace('\n', '')
            # print(line)
            reserved = ''
            if self.isPreProcessLine(line):
                reserved, line = self.getReservedPart(line)
            for replace in self.keywords:
                line = line.replace(replace, self.keywordMatch[replace])
            toWrite += (reserved + line + '\n')
        logger.debug(f'Confused Code:\n{toWrite}')
        return toWrite

    @logger.catch
    def __init__(self, level) -> None:
        self.UsedName = []
        self.confuse_level = level
        self.keywords = confuseKeywords
        self.keywordMatch = {}
        for item in self.keywords:
            self.keywordMatch[item] = self.genRandName()
        logger.debug(f'Keyword Match: {dumps(self.keywordMatch, indent=4)}')