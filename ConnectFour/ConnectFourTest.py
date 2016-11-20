#!/usr/bin/env python
# Tests for ConnectFour.py
import unittest
import ConnectFour

class ConnectFourTest(unittest.TestCase):
    def setUp(self):
        self.newGame = ConnectFour(7,3)

    def test_play_game(self):
        self.newGame.play()
        
if __name__ == '__main__':
    unittest.main()