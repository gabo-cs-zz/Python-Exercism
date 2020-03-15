def is_armstrong_number(number):
    number_to_s = str(number)
    digits_sum = sum(int(digit)**len(number_to_s) for digit in number_to_s)
    return digits_sum == number
