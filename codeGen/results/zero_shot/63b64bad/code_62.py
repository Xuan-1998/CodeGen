code
import sys

def sequence_simulation(n, seq):
    for i in range(2, n+1):
        x = 1
        y = 0
        while True:
            if x <= 0 or x > i:
                return -1
            x += seq[x]
            y += seq[x]
            x -= seq[x]
    return y

n = int(input())
seq = list(map(int, input().split()))
for i in range(n-1):
    print(sequence_simulation(i+2, [0]+list(seq)))
