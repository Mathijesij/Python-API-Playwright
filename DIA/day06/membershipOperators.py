l = [2,3,4,5,5,6,7]
l1 = [3,5,8]
for i in l:
    if i not in l1:
        l1.append(i)
print("Unique list: ",l1)

l2 = [1,2,3,4,5,5,6,6,6,6,7]
l3 =[]
count = 0
for i in l2:
    if i in l3:
        count += 1
    else:
        l3.append(i)

print("Unique values in list: ",l3)
print("Repeated count: ",count)