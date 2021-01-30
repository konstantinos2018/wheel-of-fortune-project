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