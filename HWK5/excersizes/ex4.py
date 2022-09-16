class Add(int):
    def __init__(self,number):
        super(Add, self).__init__()
        self.number = number

    def __call__(self,arg):
        new = self.number+arg
        return Add(new)

print(Add(10))

print(Add(11)(20))

print(Add(12)(21)(5))
