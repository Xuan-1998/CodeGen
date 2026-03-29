import sys

MOD = 10**9 + 7

def getLength(n, m):
    count = [0 for _ in range(10)]
    res = 0
    while n > 0:
        for d in str(n):
            count[int(d)] += 1
        newN = ''
        for i in range(10):
            if count[i] > 0:
                newN += str(i+1) * (count[i] - 1)
                count[i] -= 1
                while count[i]:
                    newN += '9'
                    count[i] -= 1
                break
        n = int(newN)
        res += 1
    return min(res, m)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(getLength(n, m) % MOD)
