def generate_permutation(n):
    permutation = list(range(1, n+1))
    for x in range(2, n+1):
        if x % 2 == 0:
            permutation[0], permutation[x//2] = permutation[x//2], permutation[0]
        else:
            permutation[0], permutation[(x-1)//2 + 1] = permutation[(x-1)//2 + 1], permutation[0]
    return ' '.join(map(str, permutation))

n = int(input())
print(generate_permutation(n))
