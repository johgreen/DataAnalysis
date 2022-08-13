import numpy as np


def loan_projection(initial_loan, apy, monthly_payment):
    '''
    Determines time to pay back loans and how much you'll pay in interest.
    '''
    initial_ = initial_loan
    new_loan_amount = initial_loan
    apy = apy/100
    monthly_int = apy/12
    num_months = 0
    total_paid = 0

    while new_loan_amount >= monthly_payment:
        
        new_loan_amount = (initial_loan * (monthly_int + 1)) - monthly_payment
        initial_loan = new_loan_amount
        total_paid += monthly_payment
        
        num_months += 1

    if new_loan_amount != 0:
        total_paid += new_loan_amount
        num_months += 1
    else:
        pass
    
    total_paid = round(total_paid, 2)

    return num_months, total_paid



months, total = loan_projection(initial_loan = 40000 , apy = 3.5, monthly_payment = 400)

print("These loans will be paid off in {} months".format(months))
print("Including interest, you'll pay ${}".format(total))




