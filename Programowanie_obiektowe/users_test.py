import unittest
from users import Users

class Users_Test(unittest.TestCase):
    def setUp(self):
        self.uzytkownicy = Users()
        self.uzytkownicy.add_user('Marta', 'm')
        self.uzytkownicy.add_user('Julia', 'j')

    def test_add_user(self):
        Users.add_user(self.uzytkownicy, 'Zuza', 'z')
        self.assertEqual(Users.show_users(self.uzytkownicy), 'Marta, Julia, Zuza')

    def test_delete_user(self):
        Users.delete_user(self.uzytkownicy, 'Julia', 'j')
        self.assertEqual(Users.show_users(self.uzytkownicy), 'Marta')

if __name__ == "__main__":
    unittest.main()
