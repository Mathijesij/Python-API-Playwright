with open('text.txt', 'r') as file:
    # read entire content
    paragraph = file.read()
    print(paragraph)

    # read line by line
    for line in file:
        print(line.strip())

# overwrite if the file exist
with open('output.txt', 'w') as file1:
    file1.write("Hello, World!\n")
    file1.write("Second line.")
    print('updated.....\n')

with open('file.csv', 'w') as csvf:
    csvf.write('Name,Age,Gender\n')
    csvf.write('Johan,23,Male\n')
    csvf.write('Emily,30,Female\n')
    csvf.write('Liam,27,Male\n')
    csvf.write('Sophie,34,Female\n')
    csvf.write('Noah,22,Male\n')
    csvf.write('Ava,28,Female\n')
    csvf.write('Ethan,31,Male\n')
    print('Csv Created and data updated......\n')

with open('file.csv', 'r') as csvr:
    readcsv = csvr.read()
    print(readcsv)

with open('file.csv', 'a') as acsv:
    acsv.write('Martha,23,Female\n')
    print('Append tha data.......\n')

with open('file.csv', 'r') as csvr:
    readcsv = csvr.read()
    print(readcsv)