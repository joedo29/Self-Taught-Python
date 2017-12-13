# Author: Joe Do

x = 'Hello World'
print(x)
len(x) # returns length of a string

# Grab everything, but go in step sizes of 1
print(x[::1])

# Grab everything, but go in step sizes of 2
print(x[::2])

# split a string by blank space
x.split()

# print string in reverse
print(x[::-1])

# you can add two string together
y = " joe"
print((x + y) * 10)

# convert a string to uppercase
print(x.upper())

# String formatting
s = 'STRING'
print('Floatting point numbers: %1.2f' %(13.144))
print('Floatting point numbers: %1.0f' %(13.144))
print('Floatting point numbers: %1.5f' %(13.144))

# Method
# general syntax
# object.methodName(arg1, arg2, ...)

# Comparison operators
a = [1, 2, 3, 4]
b = [1, 2, 3]
print(a == b) #False
print(a != b) #True
print(1 in b) #True
print(a > b) #True
print(a >= b) #True
print(a > b and 1 in b) #True
print(a > b and 1 not in b) #False
print(a > b or 1 not in b) #True

# Python Statement
c = float(input("Enter first number: "))
d = float(input("Enter second number: "))
print(c > d)
if c > d:
    print('{c} is greater than {d}'.format(c = c, d = d))
    if c < 0 and d < 0:
        print('{c} and {d} are both negative numbers'.format(c=c, d=d))
elif c == d:
    print('{c} is equal to {d}'.format(c=c, d=d))
    if c < 0 and d < 0:
        print('{c} and {d} are both negative numbers'.format(c=c, d=d))

else:
    print('{c} is less than {d}'.format(c=c, d=d))
    if c < 0 and d < 0:
        print('{c} and {d} are both negative numbers'.format(c=c, d=d))

# split a string
st = 'Print only the words that start with s in this sentence'
print(st.split())

for word in st.split():
    if word[0] == 's':
        print(word)
