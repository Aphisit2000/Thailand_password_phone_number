with open('090XXXXXXX.txt', 'w') as file:
    for i in range(10000000):
        formatted_number = '{:07d}'.format(i)
        file.write('090' + formatted_number + '\n')
