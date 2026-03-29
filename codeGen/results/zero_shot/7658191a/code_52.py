import sys

def solve():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n, k, z = map(int, sys.stdin.readline().split())
        
        arr = list(map(int, sys.stdin.readline().split()))
        
        # Initialize maximum score and current score
        max_score = 0
        curr_score = 0
        
        # Perform at most k moves
        for i in range(min(k+1, n)):
            # Add the value at the current index to the current score
            curr_score += arr[i]
            
            # Update maximum score if necessary
            max_score = max(max_score, curr_score)
            
            # If we have performed z or more moves to the left, reset the current score
            if i >= z:
                curr_score -= arr[i-z]
        
        print(max_score)

if __name__ == "__main__":
    solve()
