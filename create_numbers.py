with open('password06.txt', 'w') as file:
    for i in range(100000000):
        formatted_number = '{:08d}'.format(i)
        file.write('06' + formatted_number + '\n')

with open('password06.txt', 'w') as file:
    for i in range(100000000):
        formatted_number = '{:08d}'.format(i)
        file.write('08' + formatted_number + '\n')

with open('password09.txt', 'w') as file:
    for i in range(100000000):
        formatted_number = '{:08d}'.format(i)
        file.write('09' + formatted_number + '\n')
