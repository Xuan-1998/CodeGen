def can_obtain_b_from_a(b):
    for bi in b:
        # Try to find a segment in a with length bi
        found = False
        for i in range(len(a)):
            if len(a[i]) == bi:
                found = True
                break
        if not found:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print("YES" if can_obtain_b_from_a(b) else "NO")
