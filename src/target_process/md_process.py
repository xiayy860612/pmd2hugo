import os
import time
import re

from target_process import formatter_header, TargetProcesser
from src_content import ContentInfo, ContentType


__title_pattern = re.compile(r'^#\s+(?P<title>.+)$')
__img_pattern = re.compile(r'![[](?P<img_title>.+)[]][(](?P<img_path>.+)[)]')
__remote_src_pattern = re.compile(r'^http[s]*://.+')

def write_line(target_file, line):
    encode_line = line.encode("utf-8")
    target_file.write(encode_line)
    target_file.write('\n'.encode("utf-8"))

def __get_formatter_header_info(ab_src_path):
    formatter_header_info = {
        'title': '',
        "date": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(os.path.getmtime(ab_src_path)))
    }

    title = ''
    with open(ab_src_path, 'r', encoding='utf-8') as src_file:
        for line in src_file.readlines():
            # check title
            m = __title_pattern.match(line)
            if m is not None:
                title = m.group('title')
                break
    
    if title == '':
        title = os.path.splitext(os.path.basename(ab_src_path))[0]
    
    formatter_header_info['title'] = title
    return formatter_header_info
    
def __process_title(line):
    m = __title_pattern.match(line)
    if m is not None:
        return None
    
    return line
    
def __process_img(src_root_dir, target_root_dir, md_content_info, line):
    m = __img_pattern.match(line)
    if not m:
        return line
    
    rel_md_img_path = m.group('img_path')
    img_title = m.group('img_title')
    
    # it's img line
    m = __remote_src_pattern.match(rel_md_img_path)
    # if remote source, return orig
    if m is not None:
        return line

    # local resource, update path in static
    # should use os related separator for file path
    os_sep_rel_md_img_path = os.sep.join(rel_md_img_path.split('/'))
    md_rel_dir = os.path.dirname(md_content_info.rel_path)
    rel_md_img_path = os.path.join(md_rel_dir, os_sep_rel_md_img_path)
    # print("os sep[%s], %s" % (os.sep, rel_md_img_path))

    # process img file
    content_info = ContentInfo(ContentType.Image, rel_md_img_path)
    TargetProcesser(src_root_dir, target_root_dir).process(content_info)

    # update path
    rel_img_path = '/'.join(rel_md_img_path.split(os.sep));
    # print("md_img_path: " + rel_img_path)
    line = "![%s](/%s)" % (img_title, rel_img_path)
    return line

def process(src_root_dir, target_root_dir, content_info):

    content_root_dir = os.path.join(target_root_dir, "content")
    ab_target_path = os.path.join(content_root_dir, content_info.rel_path)
    ab_target_dir = os.path.dirname(ab_target_path)

    if not os.path.exists(ab_target_dir):
        os.makedirs(ab_target_dir)

    ab_src_path = os.path.join(src_root_dir, content_info.rel_path)
    formatter_header_info = __get_formatter_header_info(ab_src_path)

    # create hugo md file with formatter header
    formatter_header.process(ab_target_path, formatter_header_info)

    # write content from source to hugo md file
    with open(ab_src_path, 'r', encoding='utf-8') as src_file:
        with open(ab_target_path, 'ab+') as target_file:
            for line in src_file.readlines():
                line = __process_title(line)
                # ignore title line
                if not line:
                    continue
                
                line = __process_img(src_root_dir, target_root_dir, content_info, line)
                line = line.encode('utf-8')
                target_file.write(line)
        
