def generate_numbers(n):
    numbers = []
    for i in range(10**n):
        num_str = ""
        for _ in range(n):
            num_str += str(i % 10)
            i //= 10
        numbers.append(int(num_str))
    return numbers

def count_blocks(num):
    blocks = [1]  # Initialize with a block of length 1
    for i in range(1, len(str(num))):
        if str(num)[i-1] == str(num)[i]:
            blocks[-1] += 1  # Extend the current block
        else:
            blocks.append(1)  # Start a new block
    return blocks

def get_final_result(n):
    numbers = generate_numbers(n)
    block_counts = [count_blocks(num) for num in numbers]
    total_count = [0] * n
    for blocks in block_counts:
        for i, count in enumerate(blocks):
            total_count[i] += count % 998244353
    return total_count

n = int(input())  # Read the input value of n
result = get_final_result(n)
print(*result, sep=' ')  # Print the final result with spaces between each block count
