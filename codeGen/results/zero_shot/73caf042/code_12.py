python
def total_diamonds():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        total_diamonds = 0
        
        for i in range(1, N+1):
            even_sum = sum(int(digit) for digit in str(i) if int(digit)%2==0)
            odd_sum = sum(int(digit) for digit in str(i) if int(digit)%2!=0)
            
            room_number = i
            total_diamonds += abs(even_sum - odd_sum)
        
        print(total_diamonds)

total_diamonds()
