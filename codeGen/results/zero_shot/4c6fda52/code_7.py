def min_changes_to_find_substring(n, k):
    s = input().strip()
    
    # Initialize variables to keep track of the number of 'R', 'G', and 'B' characters
    r_count, g_count, b_count = 0, 0, 0
    
    # Iterate through the string and count the number of each character
    for char in s:
        if char == 'R':
            r_count += 1
        elif char == 'G':
            g_count += 1
        else:
            b_count += 1
    
    # Calculate the minimum number of characters to change
    min_changes = max(r_count - k, g_count - k, b_count - k)
    
    return min_changes

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(min_changes_to_find_substring(n, k))
