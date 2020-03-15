from math import sqrt


def score(x, y):
    distance = sqrt(x**2 + y**2)
    if landed(distance, 0, 1):
        return 10
    if landed(distance, 1, 5):
        return 5
    if landed(distance, 5, 10):
        return 1
    return 0


def landed(number, min, max):
    return min <= number <= max
