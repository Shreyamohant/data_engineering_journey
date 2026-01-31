import re
from logger import log

def clean_data(text):

    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    cleaned = " ".join(cleaned.split())

    log("Data cleaned")

    return cleaned
