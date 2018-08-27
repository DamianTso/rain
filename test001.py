
'''
Here is a small modification to test git CVS
'''


for row in range(12):
    for column in range(12-row):
        print(column, end=" ")
    print()

for row in range(12):
    for column in range(row):
        for lon in range(12-row):
            print(' ', end='')
        print('*', end='')
    print()

for row in range(12):
    for column in range(12 - row):
        print('*', end='')
    for left in range(row):
         print(row, end='')
    print()
for item in range(100):
    if item % 7 == 0:
        print()
    else:
        print(item, end=' ')
