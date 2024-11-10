def reverse(s):
    words = s.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
n = input()
print(reverse(n))