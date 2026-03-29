def can_obtain_b(b):
    n = len(b)
    for i in range(1, n):
        if abs(b[i] - b[0]) != i:  # Check if segment lengths are correct
            return True
    return False

t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    if can_obtain_b(b):
        print("YES")
    else:
        print("NO")
