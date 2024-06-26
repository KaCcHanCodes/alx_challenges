rows = 5
column = 1

while rows > 0:
    while column < 10:
        for space in range(1, rows):
            print(end=' ')
        for i in range(1, column + 1):
            print('*',end='')
        print()
        column += 2
        rows -= 1