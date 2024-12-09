c = 0


def ost(a, b):
    global c
    if a % b != 0:
        c += 1
        return ost(a - 1, b)
    return c


print(ost(74, 53))  # 1


s = input().split()
s = [int(x) for x in s]
s.remove(max(s))
print(max(s))   # 2