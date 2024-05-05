from collections import defaultdict

def max_hedgehog_beauty(n, edges):
    memo = defaultdict(int)
    memo[1] = 1  # base case: single vertex is a hedgehog with beauty 1

    for u, v in edges:
        for i in range(2, min(u, v) + 1):  # consider all possible tail lengths
            if (u, v) not in memo[i - 1]:  # edge does not connect to the end of the current tail
                memo[i] = max(memo[i], memo[i - 1] * i)
            else:  # edge connects to the end of the current tail
                updated_tail_length = u if v == i - 1 else v
                memo[i] = max(memo[i], memo[updated_tail_length - 1] * (i - updated_tail_length))

    return memo[n]
