def swaparrays(A, B):
    A, B = B, A
    return A, B
import random
A = [random.randint(0, 10) for _ in range(10)]
B = [random.randint(0, 10) for _ in range(10)]

print(A)
print(B)

A, B = swaparrays(A, B)

print(A)
print(B)