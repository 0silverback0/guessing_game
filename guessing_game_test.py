#!/usr/bin/env python3

import unittest
from unittest import mock
from guessing_game import guess

class Guessing_Game_Test(unittest.TestCase):
   def test_guess(self):
       with mock.patch('builtins.input', return_value = 3):
           self.assertEqual(guess(),3)

unittest.main()