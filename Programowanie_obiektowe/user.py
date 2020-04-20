# Klasa użytkownika
from budget import Budget

class User():
    def __init__(self, login, password):
        self.login = str(login)
        self.password = str(password)
        self.budzet = Budget()

    def change_password(self, password):
        password = str(password)
        if password == self.password:
            raise ValueError('Nowe hasło nie może być takie same!')
        else:
            self.password = password

    def show_budget(self):
        return self.budzet.plan_budget() + '\n' + self.budzet.real_budget()

    def clear_budget(self):
        self.budzet = Budget()

    def show_trans(self):
        return self.budzet.show_transactions()

    def add_inc(self, category, t, amount, day):
        return self.budzet.add_income(category, t, amount, day)

    def add_exp(self, category, t, amount, day):
        return self.budzet.add_expense(category, t, amount, day)

    def show_warnings(self):
        return self.budzet.warnings()

if __name__ == "__main__":
    uzytkownik = User()