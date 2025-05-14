def create_taci_file(file_output = ''):
    with open(file_output, 'w') as file:
        import random
        row = random.randint(3, 99)
        file.write(str(row) +'\n')
        numbers = random.sample(range(0, pow(row, 2)), pow(row, 2))
        for i in range(len(numbers)):
            file.write(str(numbers[i]) +' ')
            if (i + 1) % row == 0:
                file.write('\n')
    

if __name__ == '__main__':
    for i in range(1, 4, 1):
        
        create_taci_file(f'taci{i}.txt')
