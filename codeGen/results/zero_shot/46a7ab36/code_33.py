def generate_words(n, m):
    total_possible_words = 1
    for i in range(m):
        if i % 2 == 0:  # even index
            total_possible_words *= n  # choose any letter from the alphabet
        else:  # odd index
            for j in range(i // 2, n):  # choose a letter with an index greater than or equal to i // 2
                total_possible_words *= (n - j)
    return total_possible_words % (10**8 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = generate_words(n, m) % (10**8 + 7)
    print(result)
