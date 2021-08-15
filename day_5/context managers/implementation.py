from contextlib import contextmanager

@contextmanager
def count_line_in_file(filename):
    counter = 0
    file = open(filename)
    for line in file:
        counter += 1
    print(counter)
    yield
    file.close()

with count_line_in_file('log.txt'):
    pass