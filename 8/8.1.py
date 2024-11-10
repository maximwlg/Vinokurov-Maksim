def count_numbers(N, a, b, c):
    count = 0
    for i in range(100, N+1):
        if all(num in str(i) for num in [str(a), str(b), str(c)]):
            count += 1
    return count

print(count_numbers(220, 1, 2, 0))