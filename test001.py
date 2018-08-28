
'''
Here is a small modification to test git CVS

Print using format with a number of digits padding

print("message{:number of digits per column}.format(item to be printed)", *args, **kwargs)
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

# Use of format to print with padding (the column has a 6 digitd width, and is right justified)
for item in range(1,100):

        print("{:6d}".format(item), end=' ')
        if item % 7 == 0:
            print("\n")
