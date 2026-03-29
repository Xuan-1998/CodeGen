import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

can_merge = True
a, b = [], []
for x in p:
    if len(a) < n and len(b) < n:  # both arrays are not full
        if a and a[-1] <= x:  # a's last element is smaller or equal
            b.append(x)
        else:
            a.append(x)
    elif len(a) >= n:  # a is full, add to b
        b.append(x)
    else:  # b is full, add to a
        a.append(x)

if a and b and set(a) & set(b):  # if there are common elements
    can_merge = False

print("YES" if can_merge else "NO")
