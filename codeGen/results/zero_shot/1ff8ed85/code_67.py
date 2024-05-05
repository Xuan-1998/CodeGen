def is_valid_sequence(a, b):
    n = len(b)
    for i in range(0, n, 2):
        segment_length = b[i]
        if i + segment_length > n or segment_length != b[i+1]:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    for a in range(1, max(b)+2):
        if is_valid_sequence(a, b):
            print("YES")
            break
    else:
        print("NO")

