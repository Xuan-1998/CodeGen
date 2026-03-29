def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Initialize maximum score
        max_score = 0
        
        # Iterate over each possible move
        for i in range(k+1):
            if i <= z:
                # If the current move is within the allowed moves to the left
                score = arr[1] + (k-i) * (arr[-2] - arr[-1])
                max_score = max(max_score, score)
            else:
                # If the current move is outside the allowed moves to the left
                score = arr[1] + (k-i+1) * (arr[-1] - arr[0])
                max_score = max(max_score, score)
        
        print(max_score)

if __name__ == "__main__":
    solve()
