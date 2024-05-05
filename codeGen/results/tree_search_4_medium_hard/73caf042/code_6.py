def calculate_diamonds(n):
    total_diamonds = 0
    
    for i in range(1, n+1):
        row = i
        col = (i % n) + 1
        
        # Calculate the sum of even digits and odd digits in room number
        even_sum = sum(int(digit) for digit in str(row) if int(digit) % 2 == 0)
        odd_sum = sum(int(digit) for digit in str(row) if int(digit) % 2 != 0)
        
        # Calculate the difference between even and odd sums
        diamond_count = abs(even_sum - odd_sum)
        
        total_diamonds += diamond_count
    
    return total_diamonds

T = int(input())
for _ in range(T):
    n = int(input())
    print(calculate_diamonds(n))
