class Loan:

    duration_in_month = None
    principal_loan_amount = None

    def __init__(self, name: str, interest_rate, loan_amount, loan_period):
        self.monthly_interest_rate = interest_rate
        self.name = name
        self.principal_loan_amount = loan_amount
        self.duration_in_month = loan_period


    def get_monthly_interest(self):
        monthly_interest = (self.monthly_interest_rate / 100) / 12
        amount = int(self.principal_loan_amount * monthly_interest)
        denumeration =  1 - (1 / (1 + monthly_interest)) ** self.duration_in_month
        total_payment = amount / denumeration
        return round(total_payment,0)

    def compute_total_payment(self):
        total_to_pay = self.get_monthly_interest() * self.duration_in_month
        return round(total_to_pay, 0)

