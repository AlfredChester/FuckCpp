from sys import exit
from time import localtime
from typing import NoReturn

def genPrintFunc(info : str):
    def func() -> NoReturn:
        print(info)
        exit(0)
    return func

def genShowHelp(helpInfo : str):
    return genPrintFunc(helpInfo)

def genShowVersion(version : str):
    return genPrintFunc(
        f'''FuckCpp v{version}
Copyright (c) 2019-{localtime().tm_year} Dr.Alfred.
Distributed under the MIT License.'''
    )

def genLogPos(log_dir : str):
    return genPrintFunc(
        f'FuckCpp runtime log directory: {log_dir}'
    )
