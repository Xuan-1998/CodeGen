def flip_to_palindrome():
    n = int(input())
    s = input().strip()
    
    # Count the number of ones at each position
    ones_at_pos = [0] * (n + 1)
    for i in range(n):
        if s[i] == '1':
            ones_at_pos[i+1] += 1
    
    flip_needed = 0
    for i in range(1, n//2 + 1):
        # If the number of ones at this position is greater than zero,
        # it means we need to flip this pair
        if ones_at_pos[i] % 2 != 0:
            flip_needed += 1
    
    print("YES" if flip_needed == 0 else "NO")

flip_to_palindrome()
