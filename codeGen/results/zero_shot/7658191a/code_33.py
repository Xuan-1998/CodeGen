def max_score(n, k, z, arr):
    # Initialize the maximum score
    max_score = arr[0]
    
    # Perform exactly k moves
    for _ in range(k):
        # Check if moving right would increase the score
        if arr[_ % n] > max_score:
            max_score += arr[(_ + 1) % n]
        else:
            # Try to move left, but not more than z times consecutively
            while _ - z >= 0 and _ < k:
                _ -= 1
            # Check if moving left would increase the score
            if _ >= 0 and arr[(_ + 1) % n] > max_score:
                max_score += arr[(_ + 1) % n]
    
    return max_score

# Read input from stdin
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
