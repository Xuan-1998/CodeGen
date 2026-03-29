import sys

def can_cross_stones(stones):
    # Sort the stones positions
    stones.sort()
    
    for i in range(1, len(stones)):
        if abs(stones[i] - stones[i-1]) > 2:
            return False
    
    return True


# Read input from standard input
n = int(sys.stdin.readline())
stones = [int(x) for x in sys.stdin.readline().split()]

if can_cross_stones(stones):
    print("YES")
else:
    print("NO")
