# author: Joe Do
# range() method in Python

for num in range(10): #print value from 0 - 9
    print(num)

for num in range(5,10): #print value from 5 - 9
    print(num)

start = 5
stop = 20
for item in range(start, stop, 2):
    print(item)

print(list(range(1,6))) # cast range to a list
