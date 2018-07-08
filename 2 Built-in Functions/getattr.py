class Cake:
    name = ''
    size = 0

cake1 = Cake()
cake1.name = "Alla's wonderfull cake"
cake1.size = 2

cake2 = Cake()
cake2.name = 'Viktor\'s superable cake'
cake2.size = 666

print(cake1.name)
print(cake2.name)

print(getattr(cake1, 'name'))
print(getattr(cake2, 'size'))

