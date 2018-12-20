import re


def abbreviate(words):
    words = re.sub("-", " ", words).split()
    letters = [word[0] for word in words]
    return ''.join(letters).upper()
