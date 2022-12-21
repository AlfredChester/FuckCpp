from utils.logger import logger
from utils.constants import *
from json import dumps
from sys import argv, exit

@logger.catch
def judgeCppValid(name: str) -> bool:
    # decide if a cpp file name is valid
    for matches in cppExtensionNames:
        if name.endswith(matches):
            return True
    return False

@logger.catch
class commandConfigs:
    ParamData = defaultParamData
    def handleParam(self, index: int) -> None:
        pType = paramType[self.argv[index]]
        pName = paramName[self.argv[index]]
        if pType == 'function':
            functionMap[pName]()
        elif pType == 'data':
            try:
                data = argv[index + 1]
            except IndexError:
                logger.error("Error: Given param but no data given")
            self.ParamData[pName] = data
        else:
            self.ParamData[pName] = True

    def checkParamValid(self) -> None:
        if not 'src' in self.ParamData:
            logger.error("No Input Given. FuckCpp terminated")
            exit(0)

    def __init__(self) -> None:
        self.argc = len(argv)
        self.argv = argv
        jumpInLoop = False
        for i in range(self.argc):
            if jumpInLoop:
                jumpInLoop = False
                continue
            if argv[i] in paramType:
                self.handleParam(i)
                if paramType[argv[i]] == 'data':
                    jumpInLoop = True
            elif judgeCppValid(argv[i]) and \
                (not 'src' in self.ParamData):
                self.ParamData['src'] = argv[i]
        self.checkParamValid()
        logger.debug(f'Got Param Data: {dumps(self.ParamData, indent=4)}')