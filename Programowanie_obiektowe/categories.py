## Kategorie wydatków i przychodów

class Categories():
    def __init__(self):
        self.exp_categories = ['Mieszkanie', 'Jedzenie', 'Transport', 'Długi', 'Opieka zdrowotna', 'Dzieci', 'Rozrywka',
                               'Oszczędności', 'Inne']  # expenses
        self.inc_categories = ['Wynagrodzenie', 'Premia', 'Inne']  # incomes

    def add_exp_category(self, category):
        category = str(category)
        if category not in self.exp_categories:
            self.exp_categories.append(category)
        else:
            raise ValueError('Podana kategoria już istnieje')

    def add_inc_category(self, category):
        category = str(category)
        if category not in self.inc_categories:
            self.inc_categories.append(category)
        else:
            raise ValueError('Podana kategoria już istnieje')

    def show_inc_categories(self):
        return self.inc_categories

    def show_exp_categories(self):
        return self.exp_categories

    def __str__(self):
        return 'Aktualne kategorie wydatków: {} \nAktualne kategorie przychodów: {} \n'.format(
            ', '.join(self.exp_categories), ', '.join(self.inc_categories))

if __name__ == "__main__":
    kategories = Categories()