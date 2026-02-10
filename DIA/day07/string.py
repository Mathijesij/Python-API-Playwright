word = 'I am Johan'
w = ''
for i in word:
    w = i + w
print(w)

# indexing
w1 = word[2]
print(f'Char is: {w1}')
w2 = word[-5]
print(f'Char is: {w2}')

# slicing
w3 = word[5:]
print(f'After Slicing: {w3}')

w4 = word[-6::2]
print(f'After Slicing range: {w4}')

print('Convert into upper case: ', word.upper())
print('Convert into lower case: ', word.lower())
print('Convert into swap case: ', word.swapcase())
print('Convert into capitalize: ', word.capitalize())
print('Convert into title case: ', word.title())

print(word + ' my age is 23')