# import math
# # import cmath
#
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# b2_4ac = b**2 - 4*a*c
#
# if b2_4ac > 0:
#      root1 = (-b + math.sqrt(b2_4ac)) / (2*a)
#      root2 = (-b - math.sqrt(b2_4ac)) / (2*a)
#      print(f"Root 1: {root1}")
#      print(f"Root 2: {root2}")
#
# elif b2_4ac == 0:
#      root = -b / (2*a)
#      print(f"Root: {root}")
#
# else:
#      real_part = -b / (2*a)
#      imaginary_part = math.sqrt(abs(b2_4ac)) / (2*a)
#      print(f"Root 1: {real_part} + {imaginary_part}i")
#      print(f"Root 2: {real_part} - {imaginary_part}i")
#
#     # # use cmath to handle the imaginary value
#     #  imaginary_part = cmath.sqrt(b2_4ac) / (2 * a)
#     #  print(f"Root 1: {real_part} + {imaginary_part}")
#     #  print(f"Root 2: {real_part} - {imaginary_part}")

# without using math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

b2_4ac1 = (b**2 - 4*a*c) ** 0.5

if b2_4ac1 > 0:
     root1 = (-b + b2_4ac1) / (2 * a)
     root2 = (-b - b2_4ac1) / (2 * a)
     print(f"Root 1: {root1}")
     print(f"Root 2: {root2}")

elif b2_4ac1 == 0:
     root = -b / (2*a)
     print(f"Root: {root}")

else:
     real_part = -b / (2*a)
     imaginary_part = b2_4ac1 / (2 * a)
     print(f"Root 1: {real_part} + {imaginary_part}i")
     print(f"Root 2: {real_part} - {imaginary_part}i")
