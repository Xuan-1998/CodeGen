def count_blocks(n):
    # Generate all numbers from 0 to 10^n - 1
    numbers = [int(f"{i:0{n}}") for i in range(10**n)]

    # Initialize a dictionary to store the count of blocks of each length
    block_counts = {i: 0 for i in range(1, n + 1)}

    # Iterate through each number and count the blocks
    for num in numbers:
        # Convert the number to a string
        num_str = str(num)

        # Count the blocks of each length
        for i in range(1, n + 1):
            block_counts[i] += (num_str.count(f"{'0' * i}")) % 998244353

    # Print the count of blocks of each length
    print(*[str(count) for count in block_counts.values()], sep=" ")
