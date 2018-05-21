import os

def __title_format(content):
    line = "\"title\" = \"%s\"" % content
    return line

__line_tag = "+++"
__formatter = {
    "title": __title_format,
}

def write_line(target_file, line):
    encode_line = line.encode("utf-8")
    target_file.write(encode_line)
    target_file.write('\n'.encode("utf-8"))

def process(ab_file_path, formatter_header_info):
    with open(ab_file_path, 'wb+') as target_file:
        # start line
        write_line(target_file, __line_tag)

        for key, value in formatter_header_info.items():
            if key not in __formatter:
                continue
            
            line = __formatter[key](value)
            write_line(target_file, line)

        # end line
        write_line(target_file, __line_tag)
