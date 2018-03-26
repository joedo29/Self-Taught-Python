# Author: Joe Do
# March 26, 2018
# Simple calculator

# Perform calculation
def cal(a, b, op):
    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))

# Validate the first integer input
def askFirstInt():
    while True:
        try:
            val = int(input("Please enter the first number: "))
        except:
            print("Looks like you did not enter an integer")
            continue
        else:
            break

    return val
# Validate the second integer input
def askSecondInt():
    while True:
        try:
            val = int(input("Please enter the second number: "))
        except:
            print("Looks like you did not enter an integer")
            continue
        else:
            break

    return val

# Validate operator input
def askOp():
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')
    while op not in '+-/*':
        op = input('Please enter your operation again:\
        \nChoose between "+, -, *, /" : ')

    return op

# Wrapper function
def main():
    a = askFirstInt()

    b = askSecondInt()

    op = askOp()

    print(cal(a, b, op))

if __name__ == '__main__':
    main()
