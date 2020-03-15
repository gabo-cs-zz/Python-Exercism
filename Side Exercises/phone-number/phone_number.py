import re


class PhoneNumber:
    def __init__(self, phone_number):
        self.__clean(phone_number)
        self.area_code = self.number[0:3]

    def pretty(self):
        return f'({self.number[0:3]}) {self.number[3:6]}-{self.number[6:10]}'

    def clean(self, number):
        n = re.sub('[^0-9]', '', number)
        self.number = n.lstrip('1')
        if int(self.number[3]) <= 1 or int(self.number[0]) == 0 or len(self.number) != 10:
            raise ValueError("Invalid Phone Number")

    __clean = clean
