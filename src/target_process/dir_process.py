import os
import time

from utils import file_dir_time
from target_process import formatter_header

def process(src_root_dir, target_root_dir, content_info):
    content_root_dir = os.path.join(target_root_dir, "content")
    # print("%d %s" % (content_info.content_type, content_info.rel_path))
    ab_target_dir = os.path.join(content_root_dir, content_info.rel_path)
    ab_index_path = os.path.join(ab_target_dir, '_index.md')

    if not os.path.exists(ab_target_dir):
        os.makedirs(ab_target_dir)

    # print("new Dir: " + content_info.rel_path)
        
    # if os.path.exists(ab_index_path):
    #     return

    info = os.stat(ab_target_dir)
    formatter_header_info = {
        "title": os.path.basename(ab_target_dir),
        "date": file_dir_time.get_file_create_time(ab_target_dir),
        "lastmod": file_dir_time.get_file_last_modify_time(ab_target_dir)
    }

    formatter_header.process(ab_index_path, formatter_header_info)

