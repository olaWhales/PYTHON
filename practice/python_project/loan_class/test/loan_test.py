import unittest
from practice.python_project.loan_class import loan
from practice.python_project.loan_class.loan import Loan


class TestLoan(unittest.TestCase):

    def test_if_loan_class_exist(self):
        loan.Loan("Olawale" , 0.5, 200_000 , 12)
        self.assertTrue(True)

    def test_if_loan_class_can_get_monthly_payment(self):
        loan = Loan("Olawale" , 0.5, 240 , 12)
        self.assertEqual(loan.get_monthly_interest(), 360)

    def test_if_loan_class_can_get_yearly_payment_interest(self):
        loan = Loan("Olawale" , 0.5, 240 , 12)
        self.assertEqual(loan.get_yearly_interest(), 30)

    def test_if_loan_class_can_get_monthly_expenditure(self):
        ...

