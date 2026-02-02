import re
from logger import log

def is_valid(line):
    pattern = r'^[a-zA-Z0-9\s\n]+$'
    cleaned_line = line.strip()
    if re.match(pattern, cleaned_line):
        return True
    else:
        log(f"validation failed:{cleaned_line}")
        return False
    