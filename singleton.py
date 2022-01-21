'''
Created on Jun 28, 2020

@author: gjwang
'''


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        key = (cls, str((args, kwargs)))
        if key not in cls._instances:
            cls._instances[key] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[key]


def test():
    class ServiceExample(metaclass=Singleton):
        def __init__(self, name):
            print(f"__init__ {name}")

    srv_a1 = ServiceExample("serviceA")
    srv_a2 = ServiceExample("serviceA")

    srv_b1 = ServiceExample("serviceB")
    srv_b2 = ServiceExample("serviceB")

    assert (srv_a1 == srv_a2)
    assert (srv_b1 == srv_b2)
    assert (srv_a1 != srv_b1)


if __name__ == '__main__':
    test()
