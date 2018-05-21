from src_content import ContentType

processer = {}

class TargetProcesser:

    def __init__(self, src_root_dir, target_root_dir):
        self.src_root_dir = src_root_dir
        self.target_root_dir = target_root_dir

    def process(self, content_info):
        if content_info.content_type not in processer:
            print("not support %s" % content_info.content_type)
            return
        
        processer[content_info.content_type](self.src_root_dir, self.target_root_dir, content_info)
        
