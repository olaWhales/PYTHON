import unittest

from practice.python_project.television import tv
from practice.python_project.television.tv import Television


class Test(unittest.TestCase):
    def test_if_class_Tv_exist(self):
        television = tv.Television()

    def test_if_Ac_Can_Turn_On(self):
        television = tv.Television()
        television.turn_off()
        self.assertFalse(television.is_on())

    def test_if_Ac_Can_Turn_Off(self):
        television = tv.Television()
        television.turn_on()
        self.assertTrue(television.is_on())

    def test_if_tv_can_get_channel(self):
        television = tv.Television()
        television.turn_on()
        television.get_channel()
        self.assertTrue(television.get_channel)

    def test_if_tv_can_set_channel(self):
        television = tv.Television()
        television.turn_on()
        television.set_channel(1)
        self.assertTrue(television.get_channel(), 1)

    def test_if_tv_can_channel_can_increase(self):
        television = tv.Television()
        television.turn_on()
        television.set_channel(1)
        television.set_channel(2)
        television.set_channel(3)
        self.assertEqual(television.get_channel(), 3)

    def test_if_tv_channel_can_decrease(self):
        television = tv.Television()
        television.turn_on()
        television.set_channel(5)
        television.decrease_channel(3)
        self.assertEqual(television.get_channel(), 2)

    # def test_if_tv_channel_can_set_up_to_100(self):
    #     television = tv.Television()
    #     television.turn_on()
    #     television.set_channel(102)
    #     self.assertEqual(television.get_channel(), 100)


    def test_if_tv_can_set_volume(self):
        television = tv.Television()
        television.turn_on()
        television.get_volume()
        self.assertEqual(television.get_volume(), 0)

    def test_if_tv_can_get_volume(self):
        television = tv.Television()
        television.turn_on()
        television.set_volume_level(0)
        television.get_volume()
        self.assertEqual(television.get_volume(), 0)

    def test_if_tv_volume_can_increase(self):
        television = tv.Television()
        television.turn_on()
        television.increase_voloume(3)
        self.assertEqual(television.get_volume(), 3)

    def test_if_tv_volume_can_decrease(self):
        television = tv.Television()
        television.turn_on()
        television.increase_voloume(5)
        television.decrease_volume(1)
        television.decrease_volume(1)
        self.assertEqual(television.get_volume(), 3)






