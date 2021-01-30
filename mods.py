VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        try:
            self.prizeMoney += amt
        except TypeError as e:
            print('TypeError: {}: Input should be numeric'.format(str(e)))

    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
# Write the WOFHumanPlayer class definition (part B) here

# Write the WOFComputerPlayer class definition (part C) here