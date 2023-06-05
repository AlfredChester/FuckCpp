from utils.compress import *
from utils.confuse  import *
from utils.logger   import *
from utils.param    import *

@logger.catch
def execute(conf: commandConfigs) -> None: 
    # Firstly: Mess Codes
    pData = conf.ParamData
    sourceCode = open(pData['src'], 'r', encoding='u8')
    sourceLines = sourceCode.readlines()
    confusedCode = ''
    for line in sourceLines:
        confusedCode += line
    if not pData['noConfuse']:
        Confuser = confuser(pData['level'])
        confusedCode = Confuser.genConfused(sourceLines)
    # Secondly: Zip Codes
    if pData['zipSrc']:
        confusedCode = compress(confusedCode)
    outPutFile = open(pData['output'], 'w', encoding='u8')
    outPutFile.write(confusedCode)
    outPutFile.close()
    return
