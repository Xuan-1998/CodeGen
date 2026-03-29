import sys
def countOnes(n):
    ans = 0
    for i in range(1, 10):
        ans += min(i - 1, n // i)
    return ans

n = int(sys.stdin.readline())
print(countOnes(n))
