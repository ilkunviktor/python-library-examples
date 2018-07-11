seq = [1, 2, 3, 4, 5, 6, 7]
itR = reversed(seq) # iterator
it = iter(seq) # iterator

for _ in range(len(seq)):
    print(next(itR))
    
print(itR)

for _ in range(len(seq)):
    print(next(it))
    
print(it)

for i in reversed(seq):
    print(i)
    
for i in iter(seq):
    print(i)