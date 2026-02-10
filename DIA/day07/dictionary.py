d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
# add value in dictionary
print(d)
print('Get value by key: ',d[1])  #d.get(2)
print('Get all keys: ',d.keys())
print('Get all values: ',d.values())
print('Get all the items: ',d.items())

student = {101:{'name':'johan','age':23,'gender':'male'},102:{'name':'johana','age':23,'gender':'female'}}
print(student)
print(student.get(101).get('name'))