# Author: Joe Do
# while loop in Python

while True:
    userInput = input("Wanna know how much money you make last week? Enter Y(Yes) | N(No): ")
    if userInput == "Y" or userInput == "y":
        hour = float(input("Enter working hours: "))
        rate = float(input("Enter hourly rate: "))
        result = hour * rate
        print('You make ${result} last week'.format(result=result))

    if userInput == "N" or userInput == "n":
        print("Thanks for using our payment calculator!")
        break



