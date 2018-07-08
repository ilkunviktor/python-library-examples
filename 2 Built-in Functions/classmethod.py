class C:
    @classmethod
    def f(cls, arg1, arg2):
        print(cls)
        print(arg1)
        print(arg2)

C.f(1, 2)
C().f(1, 2)