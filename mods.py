import random

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
        command = input(prompt)
        return command

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty
    
    def smartCoinFlip(self):
        n = random.randint(1, 10)

        if n > self.difficulty:
            return True
        else:
            return False
    
    def getPossibleLetters(self, guessed):
        if guessed:
            guessed = ''.join(guessed).upper()

        possible_letters = [letter for letter in LETTERS if letter not in guessed]

        if self.prizeMoney < VOWEL_COST:
            possible_letters = [letter for letter in possible_letters if letter not in VOWELS]
        
        return possible_letters
    
    def getMove(self, category, obscuredPhrase, guessed):

        possible_letters = self.getPossibleLetters(guessed)
        if len(possible_letters) == 0:
            return 'pass'
        else:    
            if self.smartCoinFlip():
                for freq in self.SORTED_FREQUENCIES[::-1]:
                    if freq in possible_letters:
                        return freq

            else:
                return random.choice(possible_letters)