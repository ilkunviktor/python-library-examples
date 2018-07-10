def MyMul(number):
    return number * 3
#   yield number * 3 -> return generator object

l = range(10)
m = map(MyMul, l)
print(list(m))