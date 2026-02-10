# import random
#
# random_number = random.randint(1,5)
# user_input = int(input("Enter your number: "))
#
# if user_input == random_number:
#     print('You Won 🙌👍 ')
# else:
#     print('Try Again 🫡🫡')

# import pyfiglet
#
# word = pyfiglet.figlet_format("Jessie")
# print(word)

# import pyjokes
#
# joke = pyjokes.get_joke()
# print("😂", joke)

# import turtle
#
# t = turtle.Turtle()
# for i in range(36):
#     t.forward(100)
#     t.right(170)
# turtle.done()

# import matplotlib.pyplot as plt
#
# plt.plot([1, 2, 3], [-1, 4, -3])
# plt.show()

# import numpy as np
#
# arr = np.array([1, 2, 3])
# print('Mean of the given array: ',np.mean(arr))
#
# print('Maximize number of given array: ',np.max(arr))

# import datetime
#
# print(datetime.datetime.now())
#
# d1 = datetime.date(2002, 3, 24)
# d2 = datetime.date(2002, 5, 9)
# delta = d2 - d1
#
# print("Days between:", delta.days)


# import pandas as pd
#
# s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)
#
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35]
# }
# df = pd.DataFrame(data)
# print(df)

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [-3, 4, 8, -3, 6]

# plt.plot(x, y)
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# labels = ['A', 'B', 'C']
# values = [150.34, 24.5656, 103.456]
#
# plt.bar(labels, values, color='purple')
# plt.title("Bar Chart Example")
# plt.show()

# labels = ['Apples', 'Bananas', 'Cherries','Orange','Plums','Amala']
# sizes = [30.7687, 40.768767, 30.77656,45.6576,34.6866,67.76677]
#
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title("Fruit Pie Chart")
# plt.axis('equal')
# plt.show()

import random

def generate_sin():
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


print(generate_sin())





