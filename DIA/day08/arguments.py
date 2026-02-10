# def by_arg(*args):
#     for arg in args:
#         print(arg)
#         print(type(arg))
# by_arg(eval(input('Enter: ')))

def by_kwarg(**kwargs):
    for k,v in kwargs.items():
        print(f'key:{k}\tvalue:{v}')
uinput = eval(input('Enter the dict: '))
by_kwarg(**uinput)

