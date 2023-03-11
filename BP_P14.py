# Basic Python Program

# Print Patterns using Loop

'''
*
* *
* * *
* * * *
'''

rows = int(input("Enter patterns row: "))       # get patterns rows from user

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")
