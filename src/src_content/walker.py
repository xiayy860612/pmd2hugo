
import os
from collections import deque
from .content import ContentInfo, ContentType

class SrcWalker:
    """
    check dir and its sub items in recursion
    """
    def __init__(self, root_dir):
        self.__root_dir = root_dir
        self.__dir_queue = deque()
        self.__dir_queue.append("")

    def run(self):
        rel_dir_path = self.__get_dir_from_queue()
        while rel_dir_path != None:
            for src_content in self.__process_dir(rel_dir_path):
                if not src_content:
                    continue
                yield src_content

            rel_dir_path = self.__get_dir_from_queue()

    def __get_dir_from_queue(self):
        try:
            return self.__dir_queue.popleft()
        except:
            return None
            
    def __process_dir(self, rel_dir_path):
        if rel_dir_path.startswith("."):
            yield None
            return

        yield ContentInfo(ContentType.Dir, rel_dir_path)
        
        ab_dir_path = os.path.join(self.__root_dir, rel_dir_path)
        for sub_item in os.listdir(ab_dir_path):
            # ignore
            if sub_item.startswith("."):
                yield None
                continue
            
            ab_sub_item_path = os.path.join(ab_dir_path, sub_item)
            rel_sub_item_path = os.path.join(rel_dir_path, sub_item)
            # print("src item: " + rel_sub_item_path)
            if os.path.isdir(ab_sub_item_path):
                # ignore image directory
                if sub_item in ['img', 'imgs', 'image', 'images']:
                    yield None
                    continue
                
                self.__dir_queue.append(rel_sub_item_path)
                yield ContentInfo(ContentType.Dir, rel_sub_item_path)
            else:
                yield self.__process_file(rel_sub_item_path)
            
    def __process_file(self, rel_sub_item_path):
        file_ext = os.path.splitext(rel_sub_item_path)[1][1:]
        if file_ext == 'md':
            return ContentInfo(ContentType.MD, rel_sub_item_path)
        else:
            print("Not support %s file for %s format" % (rel_sub_item_path, file_ext))
            return None

            

        
        
        