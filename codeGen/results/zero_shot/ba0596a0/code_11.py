import sys

def frog_crosses_river(stones):
    # Validate input
    if len(stones) < 2 or len(stones) > 1100:
        print(False, file=sys.stdout)
        return

    # Initialize k and previous stone position
    prev_position = stones[0]
    k = 1

    for i in range(1, len(stones)):
        # Calculate distance between current and previous stone
        distance = stones[i] - prev_position
        
        # Check if a jump of k - 1, k, or k + 1 units is possible
        if abs(distance) != k - 1 and abs(distance) != k and abs(distance) != k + 1:
            print(False, file=sys.stdout)
            return

        # Update k and previous stone position
        prev_position = stones[i]
        k += 1

    print(True, file=sys.stdout)

# Read input from standard input
stones = list(map(int, sys.stdin.readline().split()))

frog_crosses_river(stones)
