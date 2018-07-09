class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C, A))
print(issubclass(C, B))
print(issubclass(B, A))
print(issubclass(A, C))
print(issubclass(B, C))