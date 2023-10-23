with open('06XXXXXXXX.txt', 'w') as file:
    for i in range(100000000):
        formatted_number = '{:08d}'.format(i)
        file.write('06' + formatted_number + '\n')
