with open('part1.txt', 'w') as file:
    for i in range(100000000):
        formatted_number = '{:08d}'.format(i)
        file.write('08' + formatted_number + '\n')

with open('part2.txt', 'w') as file:
    for i in range(100000000):
        formatted_number = '{:08d}'.format(i)
        file.write('09' + formatted_number + '\n')

with open('part3.txt', 'w') as file:
    for i in range(100000000):
        formatted_number = '{:08d}'.format(i)
        file.write(formatted_number + '\n')

with open('part4.txt', 'w') as file:
    for i in range(100000000):
        formatted_number = '{:08d}'.format(i)
        file.write('06' + formatted_number + '\n')

with open('CustomLIS.txt', 'w') as file:
    for i in range(10000):
        formatted_number = '{:04d}'.format(i)
        file.write('nameWIFI' + formatted_number + '\n')
