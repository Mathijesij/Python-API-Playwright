# def my_func():
#     n1 = input('Enter a char: ')
#     n = n1.lower()
#     match n:
#         case 'a' | 'e' | 'i' | 'o' | 'u':
#             print('vowel')
#         case _:
#             print('not vowel')
# my_func()

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divided(a,b):
    return a/b
def floor_div(a,b):
    return a//b

print('Choose the Option: \n 1.Add \n 2.Sub \n 3.Multiply \n 4.Divide \n 5.Floor Division')

while True:
    n = int(input("Enter your chose: "))
    if n > 5:
        print('Invalid option........')
    else:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter a number: "))

    match n:
        case 1:
            print(add(n1, n2))
        case 2:
            print(sub(n1, n2))
        case 3:
            print(multi(n1,n2))
        case 4:
            print(divided(n1,n2))
        case 5:
            print(floor_div(n1,n2))

    exit1 = input("Do you want to continue? (yes/no): ")
    if exit1 == 'no':
        break