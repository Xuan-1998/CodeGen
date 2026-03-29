import itertools

def can_send_sequence(b):
    # Iterate over all possible ways to split a into segments
    for segments in itertools.product(range(1, len(b) + 1), repeat=len(b)):
        # Initialize the result sequence
        a = [0] * (len(b) + 1)
        
        # Construct the result sequence by writing segment lengths
        for i in range(len(b)):
            a[segments[i]] = b[i]
        
        # Check if the resulting sequence matches b
        if ''.join(map(str, a)) == ''.join(map(str, b)):
            return 'YES'
    
    return 'NO'

# Read input and process each test case
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_sequence(b))
