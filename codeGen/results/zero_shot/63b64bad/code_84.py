code_block_start
import sys

def simulate_program(a):
    x = 1
    y = 0
    while x > 0 and x <= len(a):
        x += a[x]
        y += a[x]
        x -= a[x]
    return y if x > 0 else -1

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n-1):
    print(simulate_program(a[i+2:-1]))
code_block_end
