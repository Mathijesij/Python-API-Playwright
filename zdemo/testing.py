# from selenium import webdriver

# a=10
# b=20
# print(a,b)
# print(c)
# print(a+b)

# def validate_mobile_number(mobile_number):
# mobile_number = 765876987
# digits = ''.join([i for i in mobile_number if i.isdigit()])
# digits = ''
# for i in str(mobile_number):
#     if i.isdigit():
#         digits = digits + i
# print(digits)

# s = eval(input())
# print(s)
# print(type(s))

# remove duplicates
# l = [1,1,2,2,3,3,4,4,2,3,6,7,8]
# t =(2,2,3,3,4,4,5,5)
# s = set(l)
# s1 = set(t)
# print(list(s))
# print(tuple(s1))

import random

def generate_sin():
    d = [random.randint(1, 9) for _ in range(8)]
    d.append((10 - sum((x * 2 - 9 if x * 2 > 9 else x * 2) if i % 2 == 0 else x
                       for i, x in enumerate(reversed(d))) % 10) % 10)
    return ''.join(map(str, d))

print(generate_sin())
