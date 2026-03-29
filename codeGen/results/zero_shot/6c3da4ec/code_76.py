def solve():
    n = int(input())
    s = input()
    
    max_or = 0
    
    for i in range(1, n):
        # Calculate bitwise OR for contiguous substrings
        for j in range(i+1, n):
            sub1 = int(s[:i], 2)
            sub2 = int(s[i:j], 2)
            or_val = sub1 | sub2
            max_or = max(max_or, or_val)
    
    print(bin(max_or)[2:].zfill(n).lstrip('0'))
