import unittest
from budget import Budget

class Budget_Test(unittest.TestCase):
    def setUp(self):
        self.budzet = Budget()
        self.budzet.add_expense('Jedzenie', 'p', 200, 10)
        self.budzet.add_income('Wynagrodzenie', 'r', 4000, 1)

    def test_warnings(self):
        Budget.add_expense(self.budzet, 'Jedzenie', 'r', 250, 10)
        self.assertEqual(Budget.warnings(self.budzet), 'Zwróć uwagę na poniższe kategorie:\n- Jedzenie')

    def test_plan_exp(self):
        Budget.add_expense(self.budzet, 'Rozrywka', 'p', 50, 3)
        self.assertEqual(Budget.sum_of_plan_expenses(self.budzet), 250)

    def test_real_inc(self):
        Budget.add_income(self.budzet, 'Premia', 'r', 1000.90, 1)
        self.assertEqual(Budget.sum_of_real_incomes(self.budzet), 5000.90)

if __name__ == "__main__":
    unittest.main()
