"""Language: Python 2.7.18"""

"""User enters three integers for the program."""
x = int(input("Please enter an integar: "))
y = int(input("Please enter an integar: "))
z = int(input("Please enter an integar: "))


"""Takes the three integers and runs them through this equation."""
result = x + (y * z)

"""Determines if the result is negative, poitive, or zero."""
if result < 0:
    print('Negative')
elif result == 0:
    print('Zero')
else:
    print('Positive')

"""Prints the result."""
print str(result)
