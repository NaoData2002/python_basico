class InterestCalculator:
    def __init__(self, initial_amount, interest_rate, time, currency, interest_type, reinvestment, reinvestment_period):
        self.initial_amount = initial_amount
        self.interest_rate = interest_rate
        self.time = time
        self.currency = currency
        self.interest_type = interest_type
        self.reinvestment = reinvestment
        self.reinvestment_period = reinvestment_period

    def calculate_compound_interest(self):
        final_amount = self.initial_amount
        growth = 0
        investment_evolution = [self.initial_amount]  # to store the investment over time
        periods = {
            'Mensual': 12,
            'Trimestral': 4,
            'Semestral': 2,
            'Anual': 1
        }

        if self.interest_type == 'Anual':
            for _ in range(self.time):
                growth = final_amount * (self.interest_rate / 100)
                final_amount += growth + (self.reinvestment * periods[self.reinvestment_period])
                investment_evolution.append(final_amount)
        else:
            for _ in range(self.time * 12):  # Convert years to months
                growth = final_amount * (self.interest_rate / 100 / 12)  # Monthly rate
                final_amount += growth + (self.reinvestment * periods[self.reinvestment_period] / 12)  # Monthly reinvestment
                investment_evolution.append(final_amount)

        return final_amount, final_amount - self.initial_amount, investment_evolution
