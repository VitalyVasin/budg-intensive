def return_errors(filename):
    with open(filename) as file:
        gen = (line for line in file if 'ERROR' in line)
        for line in gen:
            print(line)

return_errors('log.txt')



