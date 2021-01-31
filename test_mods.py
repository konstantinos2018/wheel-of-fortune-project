import unittest
import random

from mods import WOFPlayer, WOFComputerPlayer
# from mods import VOWEL_COST, LETTERS, VOWELS

class TestWOFPlayer(unittest.TestCase):
    def test_init(self):
        p = WOFPlayer('Kostas')
        self.assertEqual((p.name, p.prizeMoney, p.prizes), ('Kostas', 0, []))
    
    def test_addMoney_1(self):
        p = WOFPlayer('Kostas')
        p.addMoney(10)
        expected = 10
        self.assertEqual(p.prizeMoney, expected)

    def test_addMoney_2(self):
        p = WOFPlayer('Kostas')
        p.addMoney('g')
        expected = 0
        self.assertEqual(p.prizeMoney, expected)

    def test_goBankrupt(self):
        p = WOFPlayer('Kostas')
        p.addMoney(10)
        p.goBankrupt()
        expected = 0
        self.assertEqual(p.prizeMoney, expected)
    
    def test_addPrize(self):
        p = WOFPlayer('Kostas')
        p.addPrize(500)
        expected = [500]
        self.assertEqual(p.prizes, expected)
    
    def test_str(self):
        p = WOFPlayer('Kostas')
        p.addMoney(10)
        expected = 'Kostas ($10)'
        self.assertEqual(p.__str__(), expected)

class TestWOFComputerPlayer(unittest.TestCase):
    def test_smartCoinFlip(self):
        p = WOFComputerPlayer('Kostas', 5)
        expected = False
        random.seed(a=1)
        self.assertEqual(p.smartCoinFlip(), expected)


    def test_getPossibleLetters_1(self):
        expected  = [letter for letter in 'FGHJKLMNPQRSTVWXYZ']
        p = WOFComputerPlayer('Kostas', 5)
        guessed = 'a b c d'.split()
        self.assertEqual(p.getPossibleLetters(guessed), expected)
    
    def test_getPossibleLetters_2(self):
        expected  = [letter for letter in 'EFGHIJKLMNOPQRSTUVWXYZ']
        p = WOFComputerPlayer('Kostas', 5)
        p.addMoney(250)
        guessed = 'a b c d'.split()
        self.assertEqual(p.getPossibleLetters(guessed), expected)
    
    def test_getPossibleLetters_3(self):
        expected  = 'pass'
        p = WOFComputerPlayer('Kostas', 5)
        guessed = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
        self.assertEqual(p.getMove('Music', 'Hello Janis Jackson', guessed), expected)
        

