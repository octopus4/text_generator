import re
from typing import List

delimiters = r"([\.\,\;\(\)\*\&\^\%\#\@\!\?\~\`\'\"\/\\\+\-\<\>\{\}\|\n])"


class Settings:
    def __init__(self, ignore_list="-", to_lower_case=True):
        self.ignore_list = ignore_list
        self.to_lower_case = to_lower_case


def tokenize(text: str, settings: Settings) -> List[str]:
    settings = settings
    ignore_list = settings.ignore_list
    to_lower_case = settings.to_lower_case
    if to_lower_case:
        text = text.lower()
    exceptions = set(ignore_list)
    text = re.sub(delimiters, r" \1", text)
    return list(filter(lambda x: x not in exceptions, text.split()))
