import unittest
from user import User

class User_Test(unittest.TestCase):
    def setUp(self):
        self.uzytkownik = User('Marta', 'M')
        self.uzytkownik.add_inc('Wynagrodzenie', 'p', 4000, 10)
        self.uzytkownik.add_exp('Jedzenie', 'r', 200, 5)

    def test_change_password(self):
        User.change_password(self.uzytkownik, 'm')
        self.assertEqual(self.uzytkownik.password, 'm')

    def test_show_budget(self):
        self.assertEqual(User.show_budget(self.uzytkownik), 'Planowane przychody: 4000.0\nPlanowane wydatki: 0'
                                                        '\nPozostaje do rozdysponowania: 4000.0' + '\n' +
                         'Rzeczywiste przychody: 0\nRzeczywiste wydatki: 200.0\nMogę jeszcze wydać do końca miesiąca: -200.0')

if __name__ == "__main__":
    unittest.main()
