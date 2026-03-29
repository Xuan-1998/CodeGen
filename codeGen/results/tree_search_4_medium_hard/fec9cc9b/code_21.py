import sys

def is_ladder(arr, l, r):
    inc = 0
    dec = 0
    for i in range(l-1, r):
        if arr[i] < arr[i+1]:
            dec += 1
            if dec == 1:
                return True
        elif arr[i] > arr[i+1]:
            inc += 1
            if inc == 1 and dec > 0:
                return True
    return False

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")
