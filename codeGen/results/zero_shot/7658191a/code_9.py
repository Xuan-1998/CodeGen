def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Step 1: Find the maximum score that can be achieved
        # We will use a greedy approach to solve this problem
        
        # Initialize the score and the current position
        score = arr[0]
        pos = 1
        
        # Loop through k moves
        for _ in range(k):
            # Move to the left z times if possible
            while z > 0 and pos - 2 >= 1:
                score += arr[pos - 2]
                pos -= 1
                z -= 1
            
            # Move to the right if possible
            if pos < n and (z == 0 or pos + 1 >= n):
                score += arr[pos]
                pos += 1
        
        print(score)
