def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    beauty_table = [[0] * (n + 1) for _ in range(n + 1)]
    last_beauty = {i: 0 for i in range(n)}

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if arr[j] not in bad_primes:
                beauty_table[i][j] = max(beauty_table[i][j], last_beauty.get(j, 0))
            else:
                beauty_table[i][j] = max(beauty_table[i][j], -1 + last_beauty.get(j, 0))

        for k in range(i):
            if arr[k] not in bad_primes and arr[j] % arr[k] == 0:
                beauty_table[i][j] -= 1
            elif arr[k] in bad_primes and arr[j] % arr[k] == 0:
                beauty_table[i][j] += 1

        for k in range(i + 1, j):
            if arr[j] % arr[k] == 0:
                beauty_table[i][j] -= (arr[j] // arr[k]) - 1
            last_beauty[j] = beauty_table[i][k]

    print(beauty_table[0][n - 1])

if __name__ == "__main__":
    solve()
