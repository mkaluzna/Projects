# Klasa Generator generuje przykładowe dane do budżetu (symulacje)
from budget import Budget
from categories import Categories
import random

class Generator():
    def __init__(self, n):
        self.budzet = Budget()
        self.n = n

    # przykładowa symulacja transakcji
    def simulation(self):
        kategorie = Categories()
        trans = ['inc', 'exp']
        p = [0.2, 0.8]
        categories_exp = kategorie.show_exp_categories()
        categories_inc = kategorie.show_inc_categories()
        types = ['r', 'p']
        days = [x for x in range(1, 32)]

        for i in range(self.n):
            tr = ''.join(random.choices(trans, p))
            t = random.choice(types)
            d = random.choice(days)
            if tr == 'inc':
                cat = random.choice(categories_inc)
                if cat == 'Wynagrodzenie' or cat == 'Premia':
                    a = random.randint(1500, 8000)
                    self.budzet.add_income(cat, t, a, d)
                else:
                    a = random.randint(10, 1000)
                    self.budzet.add_income(cat, t, a, d)
            elif tr == 'exp':
                cat = random.choice(categories_exp)
                if cat == 'Mieszkanie':
                    a = random.randint(500, 2000)
                    self.budzet.add_expense(cat, t, a, d)
                else:
                    a = random.randint(5, 500)
                    self.budzet.add_expense(cat, t, a, d)

        print('\n')
        print(self.budzet.show_transactions() + '\n')
        print(self.budzet.real_budget() + '\n' + self.budzet.plan_budget())
        print(self.budzet.show_df_exp())
        print('\n')
        print(self.budzet.show_df_inc())
        print('\n')
        print(self.budzet.show_df_details())

if __name__ == "__main__":
    generator = Generator(20)
    generator.simulation()