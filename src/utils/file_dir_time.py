import datetime
import os

from config import app_config

def get_file_create_time(ab_src_path):
    tz = datetime.timezone(datetime.timedelta(hours=app_config.time_zone))
    info = os.stat(ab_src_path)
    epoch_timestamp = info.st_ctime
    dt = datetime.datetime.fromtimestamp(epoch_timestamp, tz)
    return dt.isoformat()

def get_file_last_modify_time(ab_src_path):
    tz = datetime.timezone(datetime.timedelta(hours=app_config.time_zone))
    info = os.stat(ab_src_path)
    epoch_timestamp = info.st_mtime
    dt = datetime.datetime.fromtimestamp(epoch_timestamp, tz)
    return dt.isoformat()