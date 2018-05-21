from .processer import *

# config
from target_process import dir_process, md_process, img_process

processer[ContentType.Dir] = dir_process.process
processer[ContentType.MD] = md_process.process
processer[ContentType.Image] = img_process.process
