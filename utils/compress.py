from utils.constants import *
from utils.logger import *
import subprocess as sp
from sys import platform

@logger.catch
def compress(src: str) -> str:
     # cmd = NodeRunTime[platform] + \
     #     f" .\\js\\compress.js compress --src '{src}'"
     cmd = [ 
          NodeRunTime[platform], './js/compress.js', 
          'compress', '--src', f"'{src}'"
     ]
     ret = sp.check_output(cmd)
     return ret