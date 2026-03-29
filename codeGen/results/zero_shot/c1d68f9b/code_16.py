import sys

def solve():
    n = int(sys.stdin.readline().strip())
    moods = list(map(int, sys.stdin.readline().split()))
    
    # Step 1: Check if the number of knights is at least 3
    if n < 3:
        print("NO")
        return
    
    # Step 2: Calculate the total count of good moods (1's)
    total_good = sum(moods)
    
    # Step 3: If the total count of good moods is even, a regular polygon cannot be formed
    if total_good % 2 == 0:
        print("NO")
    else:
        print("YES")

solve()
