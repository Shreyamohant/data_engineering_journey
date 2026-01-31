import re
from logger import log

def is_valid(line):
    pattern = r'^[a-zA-Z0-9\s\n]+$'
    return bool(re.match(pattern, line.strip()))
    