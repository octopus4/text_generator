import re
from preprocessing import delimiters


def format_result(text: str):
    return re.sub(r"[ ]*" + delimiters, r"\1", text)
