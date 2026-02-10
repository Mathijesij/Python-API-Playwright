# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# cal = calendar.month(year, month)
# print(cal)

from faker import Faker

fake = Faker('en_US')

count = 0
while count < 10:
    name = fake.first_name()
    if name.startswith('J'):
        print(name)
        count += 1


# for _ in range(5):
#     f_name = fake.first_name()
#     l_name = fake.last_name()
#     print(f'Name: {f_name} {l_name}')