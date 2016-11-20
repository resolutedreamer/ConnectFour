#!/usr/bin/env python
# Tests for ConnectFour.py
import unittest
import sys
from ConnectFour import ConnectFour

class ConnectFourTest(unittest.TestCase):
    def setUp(self):
        self.newGame = ConnectFour(7,3)

    def test_setUp_success(self):
        self.assertTrue(self.newGame is not None)

    def test_print_new_board(self):
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]")
    
    def test_play(self):
        #self.newGame.play()
        self.assertTrue(True)
    
if __name__ == '__main__':
    unittest.main(buffer = True)