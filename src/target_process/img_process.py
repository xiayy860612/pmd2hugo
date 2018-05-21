import os
import shutil


def process(src_root_dir, target_root_dir, content_info):
    img_root_dir = os.path.join(target_root_dir, "static")
    ab_img_src_path = os.path.join(src_root_dir, content_info.rel_path)
    ab_img_target_path = os.path.join(img_root_dir, content_info.rel_path)

    if not os.path.exists(ab_img_src_path):
        raise "img file[%s] not existed" % content_info.rel_path
    
    ab_img_target_dir = os.path.dirname(ab_img_target_path)
    if not os.path.exists(ab_img_target_dir):
        os.makedirs(ab_img_target_dir)
    
    shutil.copyfile(ab_img_src_path, ab_img_target_path)
    