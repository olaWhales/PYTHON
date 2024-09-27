import unittest
import account


class TestAccount(unittest.TestCase):
    def test_if_Account_exists(self):
        account.Account("olawale", "ishola", "1111")

    def test_if_Account_can_deposit(self):
        acc1 = account.Account("olawale", "ishola", "1111")
        acc1.deposit(4000)
        result = acc1.check_balance()
        self.assertEqual(result, 4000)

    def test_if_account_can_deposit_negative_amount(self):
        acc1 = account.Account("olawale", "ishola", "1111")
        acc1.deposit(-4000)
        result = acc1.check_balance()
        self.assertEqual(result, 0)

    def test_if_account_can_withdraw(self):
        user = account.Account("olawale", "ishola", "1111")
        user.deposit(4000)
        user.withdraw(2000)
        result = user.check_balance()
        self.assertEqual(result, 2000)

    def test_if_account_can_withdraw_negative_amount(self):
        user = account.Account("olawale", "ishola", "1111")
        user.deposit(4000)
        user.withdraw(-2000)
        user.check_balance()
        self.assertEqual(user.balance, 4000)