import re
from preprocessing import delimiters
from typing import Callable
from typing import Dict


def format_result(text: str):
    return re.sub(r"[ ]*" + delimiters, r"\1", text)


def validate(arguments: Dict[str, str], validators: Dict[str, Callable]) -> None:
    for arg_name in validators.keys():
        validator = validators[arg_name]
        arg_value = arguments[arg_name]
        validator(arg_value)


def read_string(filename: str) -> str:
    if filename is None:
        return input()
    with open(filename, 'r', encoding='utf8') as data:
        lines = data.readlines()
        return ' '.join(lines)
