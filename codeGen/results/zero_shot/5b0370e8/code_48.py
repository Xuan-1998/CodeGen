def solve():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n, k = map(int, input().split())  # Read n and k
        total_and = (1 << k) - 1  # Calculate the maximum bitwise AND value
        count = 0  # Initialize the count
        for _ in range(n):
            arr = list(map(int, input().split()))  # Read the array elements
            and_val = arr[0] & total_and  # Calculate the bitwise AND of all elements
            if and_val >= ((1 << k) - 1):  # Check if the bitwise AND is maximum
                count += 1  # Increment the count if true
        print(count % (10**9 + 7))  # Print the result modulo $10^9+7$

solve()
