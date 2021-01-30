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
    
    def __str__(self):
        return '{0} (${1})'.format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        prompt = self.__str__() + '\n\n'
        prompt += 'Category: {}\n'.format(category)
        prompt += 'Phrase: {}\n'.format(obscuredPhrase)
        prompt += 'Guessed: {}\n\n'.format(', '.join(guessed))
        prompt += 'Guess a letter, phrase, or type \'exit\' or \'pass\':'

        return input(prompt)

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty