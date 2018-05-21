#!/usr/bin/python

import sys, getopt

from config import app_config
from src_content import SrcWalker
from target_process import TargetProcesser


help_info = """
usage: python pmd2hugo.py --src=<pure md content dir> --target=<hugo root dir>

options:
    --src, abstract path of pure md content directory
    --target, abstract path of hugo root directory which contains a config file
    --help, show usage

"""

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ("src=", "target=", "help"))
        if len(opts) < 1:
            raise "missing parameters"
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print(help_info)
                sys.exit(0)
            elif opt in ('--src'):
                app_config.content_src_dir = arg
            elif opt in ('--target'):
                app_config.hugo_root_dir = arg
    except:
        print(help_info)
        sys.exit(1)
    
    walker = SrcWalker(app_config.content_src_dir)
    for info in walker.run():
        TargetProcesser(
            app_config.content_src_dir, 
            app_config.hugo_root_dir
        ).process(info)
    
    print("Done")