import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
a = [int(x) for x in input().split()]

ans = []
max_len = [0]*27
min_sub = float('inf')
total_len = 0

for i in range(n):
    for j in range(i+1, n+1):
        if all(s[i:j].count(chr(k)) <= a[k-97] for k in range(ord('a'), ord('z')+1)):
            ans.append((i+1, j))
            max_len[ord(s[i-1]) - 97] = max(max_len[ord(s[i-1]) - 97], j-i)
            total_len += j-i

min_sub = min(len(sub) for sub in ans)

max_len = max(max_len)

print(sum(1 for _ in ans) % (10**9 + 7))
print(max_len)
print(min_sub)
