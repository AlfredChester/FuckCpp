from utils.compress import *
from utils.confuse import *
from utils.logger import *

# defaultParamData = {
#     'level': 'low',
#     'output': 'confused.cpp',
#     'zipsrc': True
# }

def execute(conf) -> None: 
    # Firstly: Mess Codes
    pData           = conf.ParamData
    sourceCode      = open(pData['src'], 'r', encoding='u8')
    sourcelines     = sourceCode.readlines()
    Confuser        = confuser(pData['level'])
    confusedCode    = Confuser.genConfused(sourcelines)
    return   