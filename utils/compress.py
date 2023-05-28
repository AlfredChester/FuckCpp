import subprocess as sp
from sys import platform

from utils.constants import *
from utils.logger import *

@logger.catch
def compress(src: str) -> str:
    cmd = [
        f'{cur_dir}/lib/{NodeRunTime[platform]}',
        f'{cur_dir}/js/compress.js',
        'compress', '--src', f"'{src}'"
    ]
    ret = sp.check_output(cmd)
    if not isinstance(ret, str):
        ret = str(ret, encoding = 'utf-8')
    logger.debug(f'Compressed Code:\n{ret}')
    return ret
