def calculate_total_diamonds():
    T = int(input())
    total_diamonds = 0
    
    for _ in range(T):
        N = int(input())
        
        # Initialize sum of even digits and sum of odd digits for each room
        even_sum = [0] * (N + 1)
        odd_sum = [0] * (N + 1)
        
        # Calculate the sum of even digits and sum of odd digits for each room
        for i in range(1, N + 1):
            room_number = i
            while room_number > 0:
                digit = room_number % 10
                if digit % 2 == 0: 
                    even_sum[room_number] += digit
                else: 
                    odd_sum[room_number] += digit
                room_number //= 10
        
        # Calculate the total number of diamonds for each room
        total_diamonds_room = [abs(sum_even - sum_odd) for sum_even, sum_odd in zip(even_sum[1:], odd_sum[1:])]
        
        # Update the total number of diamonds
        total_diamonds += sum(total_diamonds_room)
    
    print(total_diamonds)

if __name__ == "__main__":
    calculate_total_diamonds()
