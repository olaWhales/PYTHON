import unittest

from practice.python_project.Air_condition import ac


class test(unittest.TestCase):
    def setUp(self):
        ac.Ac()

    def test_check_if_ac_class_exists(self):
       ac.Ac()

    def test_check_if_ac_is_off_at_initial_state(self):
        modern_ac = ac.Ac()
        self.assertTrue(ac.Ac)

    def test_check_if_ac_can_be_turn_on(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        self.assertTrue(modern_ac.operate)

    def test_check_if_ac_can_be_turn_off(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        modern_ac.power_off()
        self.assertTrue(modern_ac.operate)

    def test_if_ac_initial_status_is_16_while_on(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        self.assertEqual(modern_ac.get_temperature() , 16)

    def test_if_ac_an_can_increase_in_temperature_by_1(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        modern_ac.set_temperature(1)
        self.assertEqual(modern_ac.get_temperature() , 17)

    def test_if_ac_an_can_increase_in_temperature_by_2_at_a_time(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        modern_ac.set_temperature(2)
        self.assertNotEqual(modern_ac.get_temperature() , 18)

    def test_if_ac_an_can_increase_in_temperature_1by1(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        self.assertEqual(modern_ac.get_temperature() , 20)

    def test_if_ac_cannot_increase_in_temperature_over_30(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        self.assertNotEqual(modern_ac.get_temperature() , 32)

    def test_if_ac_can_decrease_in_temperature(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        modern_ac.set_temperature(1)
        self.assertEqual(modern_ac.get_temperature() , 19)
        modern_ac.decrease_temoerature(1)
        self.assertEqual(modern_ac.get_temperature() , 18)


    def test_if_ac_cannot_decrease_in_temperature_below_16(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        modern_ac.set_temperature(1)
        self.assertEqual(modern_ac.get_temperature() , 17)
        modern_ac.decrease_temoerature(1)
        modern_ac.decrease_temoerature(1)
        modern_ac.decrease_temoerature(1)
        self.assertNotEqual(modern_ac.get_temperature() , 14)

    def test_to_off_the_ac_while_working(self):
        modern_ac = ac.Ac()
        modern_ac.power_on()
        modern_ac.set_temperature(1)
        self.assertEqual(modern_ac.get_temperature() , 17)
        modern_ac.power_off()
        self.assertTrue(modern_ac.operate)





