import unittest
from practice.python_project.loan_class import loan
from practice.python_project.loan_class.loan import Loan


class TestLoan(unittest.TestCase):
    def setUp(self):
        loan.Loan("Olawale" , 0.5, 200_000 , 12)

    def test_if_loan_class_exist(self):
        loan.Loan("Olawale" , 0.5, 200_000 , 12)
        self.assertTrue(True)

    def test_if_loan_class_can_get_monthly_payment(self):
        loaning = Loan("Olawale", 15, 200000, 24)
        self.assertEqual(loaning.get_monthly_interest(), 9697)

    def test_if_loan_class_can_get_monthly_expenditure(self):
        loan = Loan("Olawale" , 15, 200_000 , 24)
        self.assertEqual(loan.compute_total_payment(), 232_728)

