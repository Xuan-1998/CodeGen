def polygonFormation(n, moods):
    memo = [[False] * 2 for _ in range(n + 1)]
    
    for i in range(3, n + 1):
        for b in range(2):
            if sum(moods[i - k - 1:i]) % 2 == b:
                memo[i][b] = True
                for j in range(i):
                    if not memo[j][int(sum(moods[i - 1:j])) % 2]:
                        memo[i][b] = False
                        break
    
    return "YES" if memo[n][1] else "NO"


if __name__ == "__main__":
    n = int(input())
    moods = list(map(int, input().split()))
    print(polygonFormation(n, moods))
