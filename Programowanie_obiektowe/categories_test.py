import unittest
from categories import Categories

class Categories_Test(unittest.TestCase):
    def setUp(self):
        self.kategorie = Categories()

    def test_add_category(self):
        Categories.add_exp_category(self.kategorie, 'Prezenty')
        self.assertEqual(Categories.show_exp_categories(self.kategorie),['Mieszkanie', 'Jedzenie', 'Transport', 'Długi',
                                                                         'Opieka zdrowotna', 'Dzieci', 'Rozrywka',
                                                                         'Oszczędności', 'Inne', 'Prezenty'])

if __name__ == '__main__':
    unittest.main()