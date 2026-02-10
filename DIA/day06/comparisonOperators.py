def equals_Operators(a):
    if a%2 ==0 and a>=0:
        print("The given number is positive even")
    elif a%2 != 0 and a>=0:
        print("The given number is positive odd")
    elif a%2 ==0 and a<=0:
        print("The given number is negative even")
    elif a%2 != 0 and a<=0:
        print("The given number is negative odd")
    else:
        print("The given number is zero")
equals_Operators(int(input("Enter a number: ")))
