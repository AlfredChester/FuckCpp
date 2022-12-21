from json import dumps
from utils.logger import *
from random import randint

class confuser:
    def isPreProcessLine(line: str) -> bool:
        for char in line:
            if char != ' ': 
                return char == '#'
        return False

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

    def genRandName(self) -> str:
        seed = randint(0x100000, 0xffffff)
        while seed in self.UsedName:
            seed = randint(0x100000, 0xffffff)
        self.UsedName.append(seed)
        return '_' + hex(seed)

    def __init__(self, level) -> None:
        self.UsedName = []
        self.confuse_level = level
        self.keywords = confuseKeywords
        self.keywordMatch = {}
        for item in self.keywords:
            self.keywordMatch[item] = self.genRandName()
        logger.debug(f'Keyword Match: {dumps(self.keywordMatch, indent=4)}')