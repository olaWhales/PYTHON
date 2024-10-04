import unittest
import Account
from practice.python_project.pythonProject1.Test.swaptest import assertEquals
from practice.python_project.python_classwork.deposit import balance


class AccountTest(unittest.TestCase):
    def test_if_Account_exists(self):
        Account.Account("olawale" , 0.0, "1111")

    def test_if_account_can_deposit(self):
        Account.Account("olawale" , 0.0, "1111")
        Account.deposit("31111111111", 2000)
        assertEquals(balance(2000))

