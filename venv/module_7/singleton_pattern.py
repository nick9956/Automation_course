from module_4.business import *
from weakref import WeakValueDictionary
import unittest

class Singleton (type):
    _instances = WeakValueDictionary()
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Alex(Engineer, metaclass=Singleton):

    def __init__(self, name, age, sex=None, address=None):
        super(Engineer, self).__init__(name, age, sex, address)
        self.married = None

    @classmethod
    def instance(cls):
        return cls.instance()


class TestSingletonPattern(unittest.TestCase):

    def setUp(self):
        self.alex = Alex('Alex', 24)

    def tearDown(self):
        del self.alex

    def test_singleton_can_be_instantiated(self):
        assert self.alex is not None

    def test_singleton_instance_is_the_same_after_reassignment(self):
        self.alex = Alex('Alex', 25)
        assert self.alex.age == 24


    def test_singleton_instance_is_the_same_after_new_call(self):
        alex1 = Alex('Alex', 25)
        assert id(self.alex) == id(alex1)


if __name__ == '__main__':
    unittest.main()