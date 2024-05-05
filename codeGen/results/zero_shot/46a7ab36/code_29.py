import sys
input = sys.stdin.read().split()
t = int(input[0])
for _ in range(t):
    n, m = map(int, input[1:3])
    possible_words = 1
    for i in range(m):
        if i >= (2 * (i // (n - 1)) + 1):
            possible_words *= (n - 1)
        else:
            possible_words *= n
    print(possible_words % (10**8 + 7))
