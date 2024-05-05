import sys

def can_send_over_network(b):
    # Generate all possible ways to split the original sequence into segments
    for i in range(1, len(b)):
        a = [str(len(list(range(b[i-1], b[i]])))]
        a.extend(str(x) for x in range(b[i-1], b[i]))
        
        # Check if any of these generated sequences match the given sequence
        if ''.join(a) == ''.join(map(str, b)):
            return 'YES'
    return 'NO'

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    print(can_send_over_network(b))
