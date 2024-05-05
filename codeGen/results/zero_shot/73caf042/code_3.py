T = int(input())  # Read the number of test cases
for _ in range(T):
    n = int(input())  # Read the size of the grid for each test case
    total_diamonds = count_diamonds(n)
    print(total_diamonds)  # Print the result
