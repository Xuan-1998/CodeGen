import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k, z = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        
        # Calculate the maximum score by considering all possible moves
        max_score = 0
        for i in range(n - 1):
            if i < k and i < z:
                # Move left if we have more than z moves to the left
                max_score += arr[i]
            elif i >= k:
                # Stop moving when we've used up all our moves
                break
            else:
                # Move right if we're not at the end of the array and haven't used up all our moves
                max_score += arr[i + 1]
        
        print(max_score)

if __name__ == '__main__':
    solve()
