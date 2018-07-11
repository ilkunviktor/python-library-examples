class C:
    def __init__(self):
        print('invoke init')
        self._x = None
        self._y = 6

    def getx(self):
        print('invoke getx')
        return self._x

    def setx(self, value):
        print('invoke setx')
        self._x = value

    def delx(self):
        print('invoke delx')
        del self._x

    def gety(self):
        print('invoke gety')
        return self._y

    x = property(getx, setx, delx, "I'm the 'x' property.")
    y = property(fget=gety, doc="I'm the 'y' property.")

class CC:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

#    @x.deleter
#    def x(self):
#        del self._x

if __name__ == '__main__':
    c = C()
    c.x = 1
    a = c.x
    del c.x
    print(c.y)
    # c.y = 4

    cc = CC()
    cc.x = 5
    b = cc.x
    # del cc.x

    cc.x