FACTORS = {3: 'Pling', 5: 'Plang', 7: 'Plong'}


def convert(number):
    result = ''.join([FACTORS[i] for i in FACTORS if number % i == 0])
    return result or str(number)
