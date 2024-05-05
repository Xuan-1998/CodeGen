import sys

def can_cross_river(stones):
    min_jumps = [0] * len(stones)
    
    for i in range(1, len(stones)):
        min_jumps[i] = 2 ** (stones[i - 1].bit_length() + 1) - 1
        for j in range(min_jumps[i]):
            if stones[i - 1] + ((j * 3) + 1) == stones[i]:
                return True
    
    return False

# Read input from standard input
stones = [int(x) for x in sys.stdin.readline().split()]

if can_cross_river(stones):
    print("Yes")
else:
    print("No")
