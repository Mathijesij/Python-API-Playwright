l1 = [2,3,4,5,6,6,7,6,5]
l2 = []
count = 0
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        count +=1
print(f'Unique values from the list: {l2}')
print('Repeated Count: ', count)

# indexing
print('The value contains in index 3:' ,l1[3])

# slicing
print('After slicing: ',l1[3:8])

# heterogenous
l3 = ['a',[64,34,56,56,67],'ban',['apple','orange'],{3,4,5,5,6,6,7},('oo','aa'),{1:'a',2:'b'}]
print(l3)
print(l3[1][2])

# sort the list
l4 = [0,9,8,7,6,5,4,3,5,6,7,8,2,1,3]
l4.sort()
print(l4)

# typecasting
s='hello'
print(list(s))
