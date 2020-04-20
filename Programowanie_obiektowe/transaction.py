## Transakcja przychodu/wydatku

class Transaction():
    def __init__(self, category, t, amount, day):
        t = str(t)
        if t == 'r' or t == 'p':
            self.t = t
        else:
            raise ValueError('Typ budżetu może być rzeczywisty lub planowany (r/p)')

        day = int(day)
        if day < 1 or day > 31:
            raise ValueError('Dzień jest liczbą z zakresu 1-31')
        self.day = day

        category = str(category)
        self.category = category

        amount = float(amount)
        if amount < 0:
            raise ValueError('Kwota nie może być mniejsza od zera!')
        self.amount = amount

    def __str__(self):
        return 'Kategoria: {}, Typ transakcji: {}, Kwota: {}, Dzień: {}'.format(self.category, self.t, self.amount, self.day)

    def check_amount(self):
        return self.amount

    def check_category(self):
        return self.category

    def check_day(self):
        return self.day

    def check_type(self):
        return self.t
