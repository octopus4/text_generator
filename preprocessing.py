import re
from typing import List


class Settings:
    def __init__(self, ignore_list=".,;()*&^%#@!?~`'\"/\\+-<>{}|\n", exceptions="", to_lower_case=True):
        self.ignore_list = ignore_list
        self.exceptions = exceptions
        self.to_lower_case = to_lower_case


def tokenize(text: str, settings: Settings) -> List[str]:
    settings = settings
    ignore_list = settings.ignore_list
    exceptions = settings.exceptions
    to_lower_case = settings.to_lower_case
    if to_lower_case:
        text = text.lower()
    ignore_tokens = set(list(ignore_list))
    exception_tokens = set(list(exceptions))
    pattern = '[' + ignore_list + ']'
    text = re.replace()
    for ignore_token in ignore_tokens:
        text = text.replace(ignore_token, ' ' + ignore_token)
    ignore_tokens = ignore_tokens.difference(exception_tokens)
    return list(filter(None, text.split()))
