def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]

    # Initialize the dp array
    from collections import defaultdict
    dp = defaultdict(set)
    
    # Base case: all elements from 1 to 2^n are possible initially
    initial_mask = (1 << (2 ** n)) - 1
    for num in range(1, 2 ** n + 1):
        dp[(0, initial_mask)].add(num)
    
    # Transition through each bit in the string s
    for i in range(n):
        next_dp = defaultdict(set)
        for mask in dp:
            current_set = dp[mask]
            step = 2 ** (n - i - 1)
            for j in range(0, 2 ** n, 2 * step):
                for k in range(j, j + step):
                    if s[i] == '0':
                        # Keep the smaller one
                        new_value = min(current_set & {k + 1, k + step + 1})
                    else:
                        # Keep the larger one
                        new_value = max(current_set & {k + 1, k + step + 1})
                    new_mask = mask & ~(1 << k) & ~(1 << (k + step))
                    next_dp[(i + 1, new_mask)].add(new_value)
        dp = next_dp

    # The final mask should have only one bit set
    final_mask = 1 << (2 ** n - 1)
    result = sorted(dp[(n, final_mask)])
    
    # Print the result
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

