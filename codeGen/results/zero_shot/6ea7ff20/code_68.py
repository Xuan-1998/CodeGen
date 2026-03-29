n = int(input())
p = list(map(int, input().split()))
counts = {}
for pi in p:
    counts[pi] = counts.get(pi, 0) + 1

is_mergable = True
for count in counts.values():
    if count % 2 != 0 and count > 0:
        is_mergable = False
        break

if is_mergable:
    print("YES")
else:
    print("NO")
