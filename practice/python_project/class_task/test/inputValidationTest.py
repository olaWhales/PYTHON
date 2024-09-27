import re
import unittest
from class_task.class_task import inputValidation

class testInputValidation(unittest.TestCase):

    def test_if_inputValidation_Exist(self):
        actual = "2Lawale"
        expected = False
        inputValidation.validation()
        self.assertEqual(actual, expected)