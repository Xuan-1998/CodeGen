def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Initialize variables
        max_score = 0
        left_moves = 0
        
        # Simulate moves to the right as much as possible
        for i in range(k):
            if i < z:
                max_score += a[i]
            else:
                break
        
        # Try to minimize moves to the left
        for i in range(n-1, -1, -1):
            if left_moves >= z or i == 0:
                break
            max_score += a[i]
            left_moves -= 1
        
        print(max_score)

if __name__ == "__main__":
    solve()
