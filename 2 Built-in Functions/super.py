class A:
    def method(self, arg):
        print('A method', arg)

class C(A):
    def method(self, arg):
        super().method(arg)
        print('B method', arg)

c = C()
c.method('hello')