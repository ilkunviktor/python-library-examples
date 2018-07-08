class Cl:
    arr = {1, 2, 3}
    name = 'vauu'

c1 = Cl()
c1.name = '1'
c2 = Cl()
c2.name = '1'
c3 = Cl()
c3.name = '2'
h1 = hash(c1)
h2 = hash(c2)
h3 = hash(c3)
print(h1)
print(hash(c1))
print(h2)
print(hash(c2))
print(h3)