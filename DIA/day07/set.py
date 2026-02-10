s1 = {2,4,5,3,2,1,4,5}
s2 = {3,5,6,5,8,9}
print(s1)

s1.add(0)
print('After added using add: ', s1)

s1.update({6,7})
print('After add element using update:', s1)

s3 = s1.union(s2)
print('Union two set: ',s3)

# type casting
print('Convert set to list: ', list(s1))
print('Convert set to tuple: ', tuple(s1))

