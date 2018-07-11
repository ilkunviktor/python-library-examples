ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
it = iter(ls)

for _ in range(len(ls)):
    print(next(it))