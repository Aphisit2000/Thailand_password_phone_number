with open('passwordLIS.txt', 'w') as file:
    for i in range(10000):
        formatted_number = '{:04d}'.format(i)
        file.write('nameWIFI' + formatted_number + '\n')
