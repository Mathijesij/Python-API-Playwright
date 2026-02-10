def logical(a,b):
    if a>=0 and b>=0:
        print("Both a and b are greater then zero")
    elif a<=0 and b<=0:
        print("Both a and b are lesser than zero ")
    elif a==0 and b==0:
        print("Both are not equal to zero")
    elif a>0 or b>0:
        print("One of the number is negative")
logical(int(input("Enter a number:")), int(input("Enter a number:")))