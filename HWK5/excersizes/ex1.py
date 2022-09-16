# creates an instance only if ther isno instance created so far
# other wise it will return the instance that is a;ready created
class SingletonClassic(object):
    instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClassic, cls).__new__(cls)
        return cls.instance


# SingletonChild has the same instance of SingletonClass and also shares the same state
class SingletonClassic_v2(SingletonClassic):
    pass


class SingletonBase(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonChildBase(SingletonBase):
    pass

class SIngletonCall(type):
    _instance = {}
    def __call__(cls,*args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SIngletonCall,cls).__call__(*args,**kwargs)
        return cls._instance[cls]

print("singleton classic a and a_prime")
a = SingletonClassic()
a_prime = SingletonClassic()
print(a is a_prime)
print(id(a) == id(a_prime))

print("singleton classic b and b_prime")
b = SingletonClassic_v2()
b_prime = SingletonClassic_v2()
print(b is b_prime)
print(id(b) == id(b_prime))

print("singletonBase d and d_prime")
d = SingletonChildBase()
d_prime = SingletonChildBase()
print(d is d_prime)
print(id(d) == id(d_prime))

print("singletonCall c and c_prime")
c = SingletonChildBase()
c_prime = SingletonChildBase()
print(c is c_prime)
print(id(c) == id(c_prime))