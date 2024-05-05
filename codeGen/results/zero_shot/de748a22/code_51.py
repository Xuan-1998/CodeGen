import sys

def process_query(signs, l, r):
    # Calculate sign-variable sum within the range
    sign_sum = 0
    for i in range(l, r+1):
        if signs[i] == +1:
            sign_sum += 1
        else:
            sign_sum -= 1
    
    # Count +1 and -1 signs in the range
    pos_count = sum(1 for i in range(l, r+1) if signs[i] == +1)
    neg_count = sum(1 for i in range(l, r+1) if signs[i] == -1)
    
    # Find minimal number of elements to remove
    min_remove = max(0, pos_count - neg_count)
    
    return min_remove

n, q = map(int, sys.stdin.readline().split())
signs = list(map(lambda x: 1 if x == "+" else -1, sys.stdin.readline().strip()))

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    result = process_query(signs, l-1, r)
    print(result)
