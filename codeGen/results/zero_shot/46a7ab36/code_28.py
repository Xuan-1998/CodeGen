n, m = map(int, input().split())
total_possible_words = 1
for i in range(n):
    if 2*i > n:
        total_possible_words *= (n-i)
    else:
        total_possible_words *= (n-i-1)

print(total_possible_words % (10**8 + 7))
