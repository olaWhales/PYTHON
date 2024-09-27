import unittest

from class_assessment import task
from class_task.class_task import class_assessment


class testKeyCube(unittest.TestCase):
    def test_that_return_function(self):
        task([1, 2, 3, 4, 5])

    def test_that_return_dic(self):
        actual = class_assessment.task([1, 2, 3, 4, 5])
        expected = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        self.assertEqual(actual, expected)
