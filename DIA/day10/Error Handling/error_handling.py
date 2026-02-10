try:
    file = open('data.txt', 'r')
except FileNotFoundError:
    print('File not found.')
else:
    print(file.read())
    file.close()
finally:
    print('Final Part........\n')

try:
    file1 = open('file.csv','r')
except FileNotFoundError:
    print('File not found.')
else:
    print(file1.read())
    file1.close()
finally:
    print('Final Part........')
