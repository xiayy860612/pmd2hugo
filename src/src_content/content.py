
class ContentType:
    Dir = 0
    MD = 1
    Image = 2

class ContentInfo:
    def __init__(self, content_type, rel_path):
        self.content_type = content_type
        self.rel_path = rel_path


