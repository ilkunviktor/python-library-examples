class C:
    def __init__(self):
        self._a = 5

c = C()
c._a = 7
print(c._a)
setattr(c, '_a', 11)
print(c._a)