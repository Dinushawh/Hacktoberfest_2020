try:
    rows = int(input('Enter the value of n'))
    for row in range(1, rows+1):
        for column in range(1, row + 1):
            print(column, end=' ')
        print("")
except:
    print('Wrong Input')