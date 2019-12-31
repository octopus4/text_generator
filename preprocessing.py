from typing import List


class Settings:
    def __init__(self, ignore_list=".,;()*&^%#@!~`'\"/\\+-<>{}|", exceptions="", to_lower_case=True):
        self.ignore_list = ignore_list
        self.exceptions = exceptions
        self.to_lower_case = to_lower_case


class Tokenizer:
    @classmethod
    def fromfilename(cls, settings: Settings, filename: str):
        return cls(settings, "")

    def __parse_text__(self, text: str) -> List[str]:
        settings = self.__settings
        ignore_list = settings.ignore_list
        exceptions = settings.exceptions
        to_lower_case = set
        return []

    def __init__(self, settings: Settings, text: str):
        self.__settings: Settings = settings
        self.__tokens: List[str] = self.__parse_text__(text)

    def get_tokens(self):
        return self.__tokens
