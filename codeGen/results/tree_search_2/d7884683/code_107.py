def max_partitions(arr):
    n = len(arr)
    memo = {0: [0, 0]}  # Base case: fully partitioned array

    def dp(i):
        if i not in memo:
            left_sum = sum(arr[:i+1])
            right_sum = -sum(arr[i:])  # Since the array is 0-indexed
            if (left_sum, right_sum) in memo:
                memo[i] = [(k, j) for k, j in memo[(left_sum, right_sum)]]
            else:
                max_partitions = float('inf')
                for j in range(i):
                    if left_sum == sum(arr[:j+1]) and right_sum == -sum(arr[j:]):
                        partitions = dp(j-1) + 1
                        max_partitions = min(max_partitions, partitions)
                memo[i] = [(k, j) for k, j in memo[(left_sum, right_sum)]].append((max_partitions, i))
        return memo[i]

    def print_partitions(i):
        if i == n - 1:
            return
        partitions = dp(i)[0]
        for _ in range(partitions):
            print(f"Partition at index {i}:")
            left_sum = sum(arr[:i+1])
            right_sum = -sum(arr[i:])
            if left_sum > right_sum:
                print("Left: ", end='')
                print(*arr[:i+1], sep=' ')
                print("Right:", end=' ')
                print(*arr[i:], sep=' ')
            else:
                print("Right: ", end='')
                print(*arr[:i+1], sep=' ')
                print("Left:", end=' ')
                print(*arr[i:], sep=' ')
            print()
        print_partitions(i+1)

    if n % 2 == 0:
        return dp(n-1)[0]
    else:
        return -1
