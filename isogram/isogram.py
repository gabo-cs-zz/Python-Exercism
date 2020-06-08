import re


def is_isogram(string):
    string = re.sub(r'[\s-]+', '', string)
    return len(set(string.lower())) == len(string)
