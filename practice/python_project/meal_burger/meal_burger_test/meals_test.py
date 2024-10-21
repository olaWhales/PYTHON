import unittest

from practice.python_project.meal_burger import burger

class mealtest(unittest.TestCase):
    def setUp(self):
        self.burg = burger.Burger("ol")

    def testtearDown(self):
        self.assertTrue(self.burg)


    def test_to_check_BasePrice(self):
        self.burg = burger.Burger("olawale")
        self.burg.set_size('BIG') #it added self KEYWORD
        self.burg.set_base_price("BIG")
        self.assertEqual(self.burg.get_base_price() , 750)
        print (self.burg.get_base_price())

    def test_to_check_Adjusted_price(self):
        self.burg = burger.Burger("olawale")
        self.burg.set_size('MIDIUM')
        self.burg.set_adjusted_price("MIDIUM")
        self.assertEqual(self.burg.get_Adjusted_price() , 600)
        print(self.burg.get_Adjusted_price())

    def test_to_check_burger(self):
        self.burg = burger.Burger("olawale")
        self.burg.set_size('MIDIUM')
        self.extra1()
        self.extra2()
        

