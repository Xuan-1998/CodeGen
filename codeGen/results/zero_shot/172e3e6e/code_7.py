def good_subsequences(n, a):
    MOD = 10**9 + 7
    ans = 0
    for i in range(1, n+1):
        # Generate all subsequences that end at index i
        subseqs = [(j,) if j % i == 0 else () for j in range(i, n)]
        
        # Count the number of good subsequences ending at index i
        good_subseqs = sum(1 for subseq in subseqs if all(j % k == 0 for k in range(2, len(subseq)+1)))
        ans += good_subseqs
    return ans % MOD

n = int(input())
a = list(map(int, input().split()))
print(good_subsequences(n, a))
