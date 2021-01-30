import unittest

from mods import WOFPlayer

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