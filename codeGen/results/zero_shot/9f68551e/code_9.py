import sys

def min_mana_required(n):
    # Read input from stdin
    monsters = []
    for _ in range(n):
        k, h = map(int, sys.stdin.readline().split())
        monsters.append((k, h))

    # Sort monsters by appearance time
    monsters.sort(key=lambda x: x[0])

    # Initialize total mana used
    total_mana = 0

    # Iterate through monsters and calculate minimum damage required
    for k, h in monsters:
        while total_mana < h:
            total_mana += 1

    return total_mana

# Read number of test cases from stdin
t = int(sys.stdin.readline())

# Run the algorithm for each test case
for _ in range(t):
    n = int(sys.stdin.readline())
    print(min_mana_required(n))
