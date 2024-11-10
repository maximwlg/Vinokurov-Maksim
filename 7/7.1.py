def smallestodd(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return min(odd_numbers)

import random
m = [random.randint(0, 33) for _ in range(10)]
print(smallestodd(m))