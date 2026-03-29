import sys

def read_input():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        # Your logic here...
        # For now, let's just print the input values
        print(a)
        print(n)

read_input()
