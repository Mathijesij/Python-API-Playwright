import random
from faker import Faker

class resp_keyword:
    def validate_mobile_number(self, mobile_number):
        digits = ''.join([i for i in mobile_number if i.isdigit()])
        return digits

    def generate_valid_sin(self):
        digits = [random.randint(0, 9) for _ in range(8)]

        total = 0
        for i, d in enumerate(digits[::-1]):
            if i % 2 == 0:
                d *= 2
                if d > 9:
                    d -= 9
            total += d

        checksum = (10 - (total % 10)) % 10
        digits.append(checksum)

        return ''.join(map(str, digits))

    def generate_random_name(self):
        ran_first_name = self.fake.first_name()
        return ran_first_name

    def __init__(self):
        self.fake = Faker()

        self.male_titles = ['Mr', 'M', 'Sir','Mr.']
        self.female_titles = ['Mrs', 'Ms', 'Miss', 'Mlle', 'Mme']
        self.neutral_titles = ['Dr', 'Mx']

    def generate_name_by_title(self, title):
        if title in self.male_titles:
            first_name = self.fake.first_name_male()
            last_name = self.fake.last_name()
        elif title in self.female_titles:
            first_name = self.fake.first_name_female()
            last_name = self.fake.last_name()
        elif title in self.neutral_titles:
            if random.choice([True, False]):
                first_name = self.fake.first_name_male()
            else:
                first_name = self.fake.first_name_female()
            last_name = self.fake.last_name()
        else:
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()

        return first_name, last_name

    def for_get_amount(self,amount):
        amt = ''
        for i in amount:
            if i == '$':
                continue
            elif i.isdigit():
                amt = amt + i
            elif i == '.':
                break
        return amt

    def add_asset_amount(self,liquid_amt,fixed_amt):
        n1 = int(liquid_amt)
        n2 = int(fixed_amt)
        sum_amt = n1 + n2
        return str(sum_amt)



