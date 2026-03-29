import sys

def can_send_over_network():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        b = list(map(int, sys.stdin.readline().split()))
        
        if has_valid_segment(b):
            print('YES')
        else:
            print('NO')

def has_valid_segment(b):
    max_length = 0
    for i in range(len(b)):
        for j in range(i+1, len(b)+1):
            segment_sum = sum(b[i:j])
            
            if segment_sum == b[i]:
                return True
    
    return False

can_send_over_network()
