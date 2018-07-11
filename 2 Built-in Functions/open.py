with open('data/open.txt', 'w') as f:
    f.write('You touch my ta la la\n')
    print('and again!', file=f)

with open('data/open.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')