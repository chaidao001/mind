from unittest import TestCase

from utils.singleton import Singleton


class TestSingleton(TestCase):
    class TestClass(metaclass=Singleton):
        pass

    def test_singleton_twoInstances_sameHex(self):
        instance1 = TestSingleton.TestClass()
        instance2 = TestSingleton.TestClass()

        self.assertEqual(instance1, instance2)
        self.assertEqual(hex(id(instance1)), hex(id(instance2)))
