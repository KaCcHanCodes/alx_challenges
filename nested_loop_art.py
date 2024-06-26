rows = 5
column = 1

while rows > 0:                              #loop to make 5 rows (0-4)
    while column < 10:                       #loop to increase the number of stars per column (starting from 1)
        for space in range(1, rows):         #for space to match each row
            print(end=' ')
        for i in range(1, column + 1):       #to iterate through the value of column
            print('*',end='')
        print()                              #prints a new space after each iteration
        column += 2
        rows -= 1