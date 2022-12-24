import subprocess as sp
from os import path
from sys import platform

from utils.constants import *
from utils.logger import *

cur_dir = path.dirname(
     path.dirname(path.abspath(__file__))
)

@logger.catch
def compress(src: str) -> str:
     if platform == 'linux':
          import platform as pf
     cmd = [ 
          NodeRunTime[platform], f'{cur_dir}/js/compress.js', 
          'compress', '--src', f"'{src}'"
     ]
     ret = sp.check_output(cmd)
     return ret