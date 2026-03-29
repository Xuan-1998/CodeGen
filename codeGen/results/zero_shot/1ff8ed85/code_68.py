t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    for a_val in range(1, 10**9 + 1):
        if can_send([str(a_val)] * n, b):
            print("YES")
            break
    else:
        print("NO")

def can_send(a, b):
    if len(a) != len(b):
        return False
    
    for a_val, b_val in zip(a, b):
        if str(a_val) + str(b_val) != str(b_val) + str(a_val):
            return False
    return True
