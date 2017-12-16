# Author: Joe Do
# Date: Dec 16, 2017
# Purpose: Build a mini Blackjack game

import random
import string

# Explain the rules
print("Rules are simple. 1) Follow the rules of Blackjack and 2) Double the amount of your buy-in chips to win.")


# At a real casino, a blackjack deck is built by combining five single decks
# So, let's build a deck with (52*5) cards
list = [
        1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10
        ]

# Create a dealer object
class Dealer(object):
    def __init__(self, name, total):
        self.name = name
        self.total = total

    def hand(self, newCard):
        self.total += newCard

    def getTotal(self):
        return self.total

# Create a Player object to keep track of current balance, winAmount and lostAmount
class Player(object):
    def __init__(self, balance, name, total):
        self.balance = float(balance)
        self.name = name
        self.total = total

    def setWinAmount(self, bet):
        self.balance += bet

    def getWinAmount(self):
        return self.balance

    def setLostAmount(self, bet):
        self.balance -= bet

    def getLostAmount(self):
        return self.balance

    def hand(self, newCard):
        self.total += newCard

    def getTotal(self):
        return self.total

# Method to check whether player or dealer has a Blackjack
def checkBlackJack():
    if (list[0] == 1 and list[2] == 10) or (list[0] == 10 and list[2] == 1):
        return "player wins with a blackjack"
    elif (list[1] == 1 and list[3] == 10) or (list[1] == 10 and list[3] == 1):
        return "dealer wins with a blackjack"
    else:
        return "neither dealer or player has a blackjack"

# Method to ask user to continue or stop the game
def continueGame():
    while True:
        keepPlaying = input("Do you want to keep playing? Y / N: ")
        if keepPlaying.lower() not in ('Y', 'y', 'N', 'n'):
            print("Not an appropriate choice. Try again")
        else:
            break
    if keepPlaying == 'Y' or keepPlaying == 'y':
        return True
    else:
        print("Thanks for playing! Your current chips are: ", player.balance)
        return False

# Ask for player's name and how much they want to buy in
while True:
    playerName = input("Please enter your name to join the game: ")
    if playerName == '':
        print("Sorry, I didn't understand. Please use letters only without blank space!")
    else:
        break

while True:
    try:
        buyIn = float(input("How much do you want to buy in? "))
    except:
        print("Sorry, I didn't understand that. Please use numbers only!")
        continue
    else:
        break

player = Player(buyIn, playerName, 0)

print("Hi ", playerName, "! Welcome to the world of Blackjack. Your total chips are ", buyIn)

# Instantiate a new dealer
dealer = Dealer('John', 0)

# Shuffle the deck
random.shuffle(list) # Shuffle the deck before the game

print("Your dealer today is ", dealer.name, ". Your new deck is ready. Let's start the game!")

countDeck = 0
check = True
while check and player.balance > 0:
    list1 =[] # player hand
    del list1[:]
    list2 = [] # dealer hand
    del list2[:]
    while True:
        while True:
            try:
                betting = float(input("How much do you want to bet? "))
            except:
                print("Sorry, I didn't understand that. Please use numbers only!")
                continue
            else:
                break

        if betting > player.balance:
            print("You can't bet more than your current balance", player.balance, ". Please enter your bet again.")
            continue
        else:
            print("Good luck, ", player.name)
            break

    # Player gets first card
    list1.append(list[countDeck])
    countDeck += 1

    # Dealer gets first card
    list2.append(list[countDeck])
    countDeck += 1

    # Player gets second card
    list1.append(list[countDeck])
    countDeck += 1

    # Dealer gets second card
    list2.append(list[countDeck])
    countDeck += 1

    print("player has the combination of", list1)
    print('dealer has a', list2[1], "and one more card")

    # Check for player's Blackjack
    if 10 in list1 and 1 in list1:
        print("player wins with a blackjack")
        player.setWinAmount(betting)
        print("Your total chip is ", player.balance)
        if float(player.balance) >= float((buyIn * 2)):
            print("You won! Your current chips are ", player.balance)
            check = False
            break
        check = continueGame()

    # Check for dealer's Blackjack
    elif 10 in list2 and 1 in list2:
        print("dealer wins with a blackjack")
        player.setLostAmount(betting)
        print("Your total chip is ", player.balance)
        if player.balance == 0:
            print("Sorry, since your balance is now 0. The game is over.")
            check = False
            break

        check = continueGame()

    else:
        playerDecision = ''
        while playerDecision != 'S' and playerDecision != 's' and sum(list1) < 21:
            playerDecision = input("Please enter H to hit or S to stay: ")
            if playerDecision == 'H' or playerDecision == 'h':
                list1.append(list[countDeck])
                print(list1)
                countDeck += 1

        if sum(list1) > 21:
            player.setLostAmount(betting)
            print("You Lost! Your current balance is: ", player.balance)
            if player.balance == 0:
                print("Sorry, since your balance is now 0. The game is over.")
                check = False
                break
            check = continueGame()

        else:
            while sum(list2) <= 17:
                list2.append(list[countDeck])
                countDeck += 1

            if (sum(list2) > sum(list1)) and (sum(list2) <= 21) :
                print("dealer has: ", list2)
                player.setLostAmount(betting)
                print("You Lost! Your current balance is: ", player.balance)
                if player.balance == 0:
                    print("Sorry, since your balance is now 0. The game is over.")
                    check = False
                    break
                check = continueGame()

            elif sum(list1) == sum(list2):
                print("You tie!")
                check = continueGame()

            else:
                print("dealer has: ", list2)
                player.setWinAmount(betting)
                print("You win! Your current balance is: ", player.balance)
                if float(player.balance) >= float((buyIn * 2)):
                    print("You won! Your current chips are ", player.balance)
                    check = False
                    break
                check = continueGame()
