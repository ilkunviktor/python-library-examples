'''
class C:
   a = {}

c = C()
print(c.a)
c.a = {1, 2, 3}
print(c.a)
delattr(c, 'a')
print(c.a)
'''