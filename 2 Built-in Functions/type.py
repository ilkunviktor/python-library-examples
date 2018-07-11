class X:
    a = 1
    
Z = type('Z', (object,), dict(a=1))

x = X()
z = Z()

print(X)
print(Z)
print(x)
print(z)
print(type(z))