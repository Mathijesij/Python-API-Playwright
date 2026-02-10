t = ('one','two','three','four','five','one','two','seven')
print(t)
print('The index of given value: ',t.index('two'))
print("Count of 'one': ",t.count('one'))
t1 = (1,2,3,4)

# concatenate
t2 = t + t1
print('Add to two tuple: ', t2)

# type cast
print('Covert tuple to list: ',list(t))
print('Convert tuple to set: ', set(t))

t3 = ((1,'a'),(2,'b'),(3,'c'))
print('Convert tuple to dictionary: ', dict(t3))