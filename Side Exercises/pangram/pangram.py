# Determine if a sentence is a pangram.
from string import ascii_lowercase as alph
import re


def is_pangram(sentence):
    return len(set(alph) - set(sentence.lower())) == 0