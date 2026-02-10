# # Armstrong Number
# n = int(input("Enter the number: "))
# temp = n
# sum = 0
#
# while n>0:
#     n1 = n%10
#     sum = sum + n1**len(str(temp))
#     n = n//10
#
# if sum == temp:
#     print("The given number is Armstrong Number. ")
# else:
#     print("The given number is not Armstrong Number. ")

# Basic calculator
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
    if n in (1,2,3,4,5):
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter a number: "))
        if n == 1:
            print(add(n1,n2))
        elif n == 2:
            print(sub(n1,n2))
        elif n == 3:
            print(multi(n1,n2))
        elif n == 4:
            print(divided(n1,n2))
        elif n == 5:
            print(floor_div(n1,n2))
        exit1 = input("Do you want to continue? (yes/no): ")
        if exit1 == 'no':
            break
    else:
        print('Invalid Option')


