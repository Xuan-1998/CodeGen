import sys

def read():
    return [int(x) for x in input().split()]

n, m = read()
arr = read()

for _ in range(m):
    l, r = read()
    
    if all(arr[i] <= arr[i+1] for i in range(l-1, r)):
        print("Yes")
    else:
        print("No")

