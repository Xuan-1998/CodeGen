def maximum_score():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Sort the array in descending order
        arr.sort(reverse=True)
        
        score = 0
        left_moves = 0
        
        for i in range(k):
            if i < min(z, k):  # Try to make a move to the right
                score += arr[i]
            else:  # Make a move to the left to minimize impact
                score += arr[i - left_moves]
                left_moves -= 1
        
        print(score)

maximum_score()
