n = int(input())
p = list(map(int, input().split()))
counts = {}
for i in p:
    counts[i] = counts.get(i, 0) + 1

if any(count > 1 for count in counts.values()):
    print("NO")
else:
    print("YES")
