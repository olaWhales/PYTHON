import unittest
import functiontask

class testFunction(unittest.TestCase):

    def test_that_this_result_is_correct(self):
        self.assertEqual(functiontask.classwork("user"), {'u':1 , 's':1 , 'e':1 , 'r':1})

    def test_that_capital_letters_are_correct(self):
        actual = functiontask.classwork("LOVEEEds")
        expected = ({'L':1 , 'O':1 , 'V':1 , 'E':3 , 'd':1 , 's':1})
        self.assertEqual(actual, expected)