import unittest

from practice.python_project.Bike import bike


class bike_test(unittest.TestCase):
    def setUp(self):
        bike.Auto_bike()

    def test_if_bike_class_exist(self):
        bc = bike.Auto_bike()


    def test_if_bike_can_power_on(self):
        bc = bike.Auto_bike()
        start = bc.turn_on
        self.assertTrue(bc.switch)

    def test_if_bike_Can_Turn_Off(self):
        bc = bike.Auto_bike()
        start = bc.turn_off
        self.assertTrue(bc.switch)

    def test_if_bike_can_accelerate_with_gear_1(self):
        bc = bike.Auto_bike()
        start = bc.turn_on()
        self.assertTrue(bc.switch)
        current_speed = bc.acceleration_on_1(1,19)
        self.assertEqual(current_speed , 20)

    def test_if_bike_cannot_accelerate_over_20_with_gear_1(self):
        bc = bike.Auto_bike()
        start = bc.turn_on()
        self.assertTrue(bc.switch)
        current_speed = bc.acceleration_on_1(1,19)
        self.assertNotEqual(current_speed , 22)

    def test_if_bike_can_accelerate_with_gear_2(self):
        bc = bike.Auto_bike()
        start = bc.turn_on()
        self.assertTrue(bc.switch)
        current_speed = bc.acceleration_on_2(2,26)
        self.assertEqual(current_speed , 28)

    def test_if_bike_can_accelerate_with_gear_3(self):
        bc = bike.Auto_bike()
        start = bc.turn_on()
        self.assertTrue(bc.switch)
        current_speed = bc.acceleration_on_3(3,33)
        self.assertEqual(current_speed , 36)

    def test_if_bike_cannot_accelerate_over_40_with_gear_3(self):
        bc = bike.Auto_bike()
        start = bc.turn_on()
        self.assertTrue(bc.switch)
        current_speed = bc.acceleration_on_3(3,33)
        self.assertNotEqual(current_speed , 43)


    def test_if_bike_can_accelerate_with_gear_4(self):
        bc = bike.Auto_bike()
        start = bc.turn_on()
        self.assertTrue(bc.switch)
        current_speed = bc.acceleration_on_4(4,44)
        self.assertEqual(current_speed , 48)



    #
