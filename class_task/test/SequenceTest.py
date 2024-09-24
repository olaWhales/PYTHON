import unittest
from class_task.class_task import Sequence
import unittest

class TestSequence(unittest.TestCase):
    def testifSequenceIsExist(self):
        actual = 12,34,56,78,98
        expected = ['12','34','56','78','98']
        Sequence.sequence()
        self.assertEqual(actual,expected)