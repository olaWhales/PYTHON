class Loan:

    def __init__(self, name: str, interest_rate, loan_amount, loan_period):
        self.interest_rate = 0.5
        self.name = "Olawale"
        self.loan_amount = 240
        self.loan_period = 12


    def get_monthly_interest(self):
        amount = int(self.loan_amount * self.interest_rate)
        monthly_payment = int(self.loan_amount + amount)
        return monthly_payment

    def get_yearly_interest(self):
        amount = int(self.loan_amount / self.loan_period)
        payment = int(self.interest_rate * amount)
        total_payment = payment + amount
        return total_payment

    def calculate_loan_repayment(self):
        ...