def minCuts(s):
    n = len(s)
    cuts = 0
    for i in range(n):
        left, right = i, n-i-1
        while left < right:
            if s[left] != s[right]:
                if left == i:
                    cuts += 1
                    left += 1
                elif right == n - i - 1:
                    cuts += 1
                    right -= 1
                else:
                    cuts += 2
                    break
    return cuts

n = int(input())
s = input().strip()
print(minCuts(s))
