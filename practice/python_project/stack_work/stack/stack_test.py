import unittest
from practice.python_project.stack_work import stack_practice

class TestStackPractice(unittest.TestCase):
    def setUp(self):
        stack_practice.Stack(5)

    def test_to_create_stack(self):
        stack_practice.Stack(5)

    def test_to_check_if_stack_is_empty(self):
        stacks = stack_practice.Stack(5)
        stacks.is_empty()
        self.assertTrue(stacks.is_empty(), True)

    def test_to_check_if_stack_can_push_element(self):
        stacks = stack_practice.Stack(5)
        stacks.push(1)
        stacks.push(2)
        self.assertTrue(stacks.get_state(), 2)

    def test_to_check_if_stack_can_push_element_more_than_capacity(self):
        stacks = stack_practice.Stack(5)
        stacks.push(1)
        stacks.push(2)
        stacks.push(3)
        stacks.push(4)
        stacks.push(5)
        stacks.push(6)
        self.assertNotEqual(stacks.get_state(), 6)

    def test_to_check_if_stack_can_pop_element(self):
        stacks = stack_practice.Stack(5)
        stacks.push(1)
        stacks.pop()
        self.assertEqual(stacks.get_state(), [0])

    def test_to_check_if_stack_can_pop_all_element_capacity(self):
        stacks = stack_practice.Stack(5)
        stacks.push(1)
        stacks.push(2)
        stacks.push(3)
        stacks.push(4)
        stacks.push(5)
        stacks.pop()
        stacks.pop()
        stacks.pop()
        stacks.pop()
        stacks.pop()
        self.assertNotEqual(stacks.get_state(), 0)

    def test_to_check_if_stack_can_full(self):
        stacks = stack_practice.Stack(3)
        stacks.push(1)
        stacks.push(2)
        stacks.push(3)
        stacks.push(4)
        self.assertFalse(stacks.is_full(), True)

