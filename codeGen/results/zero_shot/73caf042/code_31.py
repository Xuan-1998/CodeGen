def solve():
    T = int(input())  # Read the number of test cases
    for _ in range(T):
        N = int(input())  # Read the size of the grid
        total_diamonds = 0
        for i in range(1, N*N+1):
            room_number = i
            even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            diamonds = abs(even_sum - odd_sum)
            total_diamonds += diamonds
        print(total_diamonds)

if __name__ == "__main__":
    solve()
