## Klasa budżetu (zarówno rzeczywistego jak i planowanego)
from transaction import Transaction
from tables import Tables

class Budget(Tables):
    def __init__(self):
        Tables.__init__(self)
        self.plan_incomes = []
        self.real_incomes = []
        self.plan_expenses = []
        self.real_expenses = []

    # dodanie przychodu do budżetu
    def add_income(self, category, t, amount, day):
        transakcja = Transaction(category, t, amount, day)
        if category not in self.kategorie.inc_categories:
            raise ValueError('Zmień lub dodaj kategorię!')
        elif t == 'r':
            self.real_incomes.append(transakcja)
            self.df_inc.loc[category, 'Rzeczywiste'] += amount
        elif t == 'p':
            self.plan_incomes.append(transakcja)
            self.df_inc.loc[category, 'Planowane'] += amount
        elif t is not 'r' or t is not 'p':
            raise ValueError('Typ może być "p" lub "r"')

        self.df_inc['Różnica'] = self.df_inc['Rzeczywiste'] - self.df_inc['Planowane']
        if self.df_inc.loc[category, 'Rzeczywiste'] != 0 and self.df_inc.loc[category, 'Planowane'] != 0:
            self.df_inc.loc[category, 'St. realizacji budżetu (%)'] = \
                self.df_inc.loc[category, 'Rzeczywiste'] / self.df_inc.loc[category, 'Planowane'] * 100

    # dodanie wydatku do budżetu
    def add_expense(self, category, t, amount, day):
        transakcja = Transaction(category, t, amount, day)
        if category not in self.kategorie.exp_categories:
            raise ValueError('Zmień lub dodaj kategorię!')
        elif t == 'r':
            self.real_expenses.append(transakcja)
            self.df_exp.loc[category, 'Rzeczywiste'] += amount
            self.df_details.loc[day, category] += amount
        elif t == 'p':
            self.plan_expenses.append(transakcja)
            self.df_exp.loc[category, 'Planowane'] += amount
        elif t is not 'r' or t is not 'p':
            raise ValueError('Typ może być "p" lub "r"')

        self.df_exp['Różnica'] = self.df_exp['Planowane'] - self.df_exp['Rzeczywiste']
        if self.df_exp.loc[category, 'Rzeczywiste'] != 0 and self.df_exp.loc[category, 'Planowane'] != 0:
            self.df_exp.loc[category, 'St. realizacji budżetu (%)'] = \
                self.df_exp.loc[category, 'Rzeczywiste'] / self.df_exp.loc[category, 'Planowane'] * 100

    def show_transactions(self):
        return 'Planowane przychody:\n{} \n\nPlanowane wydatki:\n{} \n\nRzeczywiste przychody:\n{} \n\nRzeczywiste wydatki:\n{}'.\
            format('\n'.join([str(x) for x in self.plan_incomes]), '\n'.join([str(x) for x in self.plan_expenses]),
                   '\n'.join([str(x) for x in self.real_incomes]), '\n'.join([str(x) for x in self.real_expenses]))

    def sum_of_plan_incomes(self):
        suma = 0
        for i in range(len(self.plan_incomes)):
            suma = suma + self.plan_incomes[i].check_amount()
        return suma

    def sum_of_real_incomes(self):
        suma = 0
        for i in range(len(self.real_incomes)):
            suma = suma + self.real_incomes[i].check_amount()
        return suma

    def plan_budget(self):
        return 'Planowane przychody: {}\nPlanowane wydatki: {}\nPozostaje do rozdysponowania: {}'.format(
            self.sum_of_plan_incomes(), self.sum_of_plan_expenses(), self.sum_of_plan_incomes() - self.sum_of_plan_expenses())

    def sum_of_plan_expenses(self):
        suma = 0
        for i in range(len(self.plan_expenses)):
            suma = suma + self.plan_expenses[i].check_amount()
        return suma

    def sum_of_real_expenses(self):
        suma = 0
        for i in range(len(self.real_expenses)):
            suma = suma + self.real_expenses[i].check_amount()
        return suma

    def real_budget(self):
        return 'Rzeczywiste przychody: {}\nRzeczywiste wydatki: {}\nMogę jeszcze wydać do końca miesiąca: {}'.format(
            self.sum_of_real_incomes(), self.sum_of_real_expenses(), self.sum_of_real_incomes() - self.sum_of_real_expenses())

    def warnings(self):
        roznice = self.df_exp['Różnica']
        lista = []
        i = 0
        while i < len(roznice):
            if roznice[i] < 0:
                lista.append(i)
            i += 1
        if len(lista) == 0:
            return 'Wszystko jest pod kontrolą!'

        chosen = [self.kategorie.exp_categories[lista[j]] for j in range(len(lista))]
        return 'Zwróć uwagę na poniższe kategorie:\n- {}'.format(('\n- ').join([x for x in chosen]))

if __name__ == "__main__":
    budzet = Budget()