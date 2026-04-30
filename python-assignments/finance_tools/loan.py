def calculate_emi(principal, annual_rate, tenure_months):
    '''Calculates Equated Monthly Installment (EMI) for a loan.'''
    monthly_rate = annual_rate / (12 * 100)
    if monthly_rate == 0:
        return principal / tenure_months
    emi = (principal * monthly_rate * ((1 + monthly_rate) ** tenure_months)) / (
                ((1 + monthly_rate) ** tenure_months) - 1)
    return emi
