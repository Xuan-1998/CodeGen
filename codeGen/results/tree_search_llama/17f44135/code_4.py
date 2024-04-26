import sys

def solve():
    n, k = map(int, input().split())
    difficulties = list(map(int, input().split()))
    
    # Initialize variables
    left, right = 0, n - 1
    max_solved = 0
    
    while left <= right:
        if difficulties[left] <= k or difficulties[right] <= k:
            max_solved += 1
            left += 1
            right -= 1
        elif difficulties[left] > k and difficulties[right] > k:
            break
        elif difficulties[left] > k:
            right -= 1
        else:
            left += 1
    
    print(max_solved)

if __name__ == "__main__":
    solve()
