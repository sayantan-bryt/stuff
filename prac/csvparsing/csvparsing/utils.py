import re


def clean_text(inp: str) -> str:
    CLEAN_REG = "\\n"
    return re.sub(CLEAN_REG, '', inp)


def list_to_dict(header:list, row:list):
    return {k: v for k, v in zip(header, row)}


def str_to_list(s:str, delimiter=',') -> list:
    return [ clean_text(item) for item in s.split(delimiter) ]


