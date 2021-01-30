import unittest
import random

from mods import WOFPlayer, WOFComputerPlayer

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

