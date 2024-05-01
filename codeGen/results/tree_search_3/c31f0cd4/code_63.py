def solve():
    N = int(input())
    numbers = list(map(int, input().split()))

    # Initialize a hashmap to store the sums and their frequencies
    sum_freq = {}

    def dfs(i, current_sum):
        if i == N:
            return

        # Calculate the sum with and without the current number
        sum_without = current_sum
        sum_with = current_sum + numbers[i]

        # Update the sum frequencies in both cases
        for s in (sum_without, sum_with):
            freq = sum_freq.get(s, 0)
            sum_freq[s] = freq + 1

        # Recursively call dfs on the remaining numbers
        dfs(i + 1, sum_without)
        dfs(i + 1, sum_with)

    # Start the DFS from an empty subset
    dfs(0, 0)

    # Print out the unique sums and their frequencies
    print(' '.join(map(str, sorted(sum_freq.keys()))))

solve()
