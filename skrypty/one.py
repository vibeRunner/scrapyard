# by M81V4N
# github.com/M81V4N

import random as r

print(r"""
  ______     |\    |   |-------
 /      \    | \   |   |
|        |   |  \  |   |-------
|        |   |   \ |   |
 \      /    |    \|   |-------
  ------
""")
print("UNO-like Card Game But Written In Python")
print("Made by M81V4N. Version 1.0")

# types of cards:
#  - Number card
#     > Number (value)
#     > Color
#  - Special card
#     > color (black can go everywhere)
#     > action (defined function to this card when placed)
#     > value (if needed)

# colors:
# red,blue,yellow,green,BLACK

# specials:
# - normal:
#   > block
#   > (order) switch
#   > plus - it have string as value "+2" or "+4"
#   > (color) change

# 40 - numbers                  up to 40
# 4 - block                     up to 44
# 4 - switch                    up to 48
# 6 - plus (including 2x black) up to 54
# 2 - change                    up to 56
# 56 at all

class Game():
    def __init__(self):
        self.countPlayers = int(input("\nCount of players: "))
        print()
        self.currentCard = Card("number",{"color":r.choice(["red","blue,","yellow",'green']), "value":r.randrange(0,10)})

        self.table = []
        for a in ["red","blue","yellow","green"]:
            for b in range(1,10):
                self.table.append(Card("number",{"value":b,"color":a,"name":str(a[0])+str(b)}))
                self.table.append(Card("number",{"value":b,"color":a,"name":str(a[0])+str(b)}))

        self.players = []
        for a in range(0,self.countPlayers):
            self.players.append(Player(input("Name of player "+str(a+1)+": ")))
        print()

        for a in self.players:
            for x in range(0,7):
                tempo = r.choice(self.table)
                a.hand.append(tempo)
                self.table.pop(self.table.index(tempo))


class Card():
    def __init__(self, type, info):
        self.type = type
        if type == "number":
            self.value = info["value"]
            self.color = info["color"]

        elif type == "switch":
            self.color = info["color"]

        elif type == "block":
            self.color = info["color"]

        elif type == "plus":
            self.color = info["color"]
            self.value = info["value"]

        #change is not needed to be specified

        else:
            print("wot you did typo somewhere m8")

    def __str__(self):
        if self.type == "number":
            return str(list(self.color)[0]) + str(self.value)

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def showHand(self):
        output = ""
        for a in self.hand:
            output += str(a) + ", "
        print(output[:-2])

    def take(self):
        a = r.choice(game.table)
        self.hand.append(a)
        game.table.remove(a)

    def place(self, opt):
        if opt == "take":
            print("u need extra card?")
            self.take()
        else:
            isMatching = False
            for a in self.hand: #string to actual card instance, searches if there is matching card
                if list(opt)[0] == list(str(a))[0] or list(opt)[1] == list(str(a))[1]:
                    print("!!!")
                    if a == game.currentCard:
                        opt = a
                        game.currentCard = a
                        self.hand.remove(a)
                        isMatching = True

            if isMatching == True:
                print("Ready! All set to go!")
            else:
                print("lol ur dumb try again")

game = Game()

while True:
    game.players[0].showHand()
    print(game.currentCard)
    game.players[0].place(input("I CHOOSE: "))
