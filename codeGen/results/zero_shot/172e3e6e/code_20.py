def good_subsequences(i, k):
    if i == 0:
        return 1
    if k < i or a[k] % i != 0:
        return 0
    return (good_subsequences(i-1, k-1) + good_subsequences(i, k-1)) % (10**9 + 7)

def solve():
    ans = [0] * (n+1)
    for i in range(1, n+1):
        if a[i-1] % i == 0:
            ans[i] = (ans[i-1] + good_subsequences(i, i-1)) % (10**9 + 7)
    return ans[-1]

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solve())
