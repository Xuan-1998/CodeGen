def can_merge(p):
    n = len(p) // 2

    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= n and j >= n:
            # Base case: permutation p matches either array a or b
            return "YES" if sorted(p[:n]) == sorted(p[n:]) else "NO"

        result = None

        if i < n:
            # Consider adding ai to p and incrementing i
            result = helper(i + 1, j)
            if result != "YES":
                continue

            # Check if current permutation is a valid merge of arrays a and b
            if sorted(p[:i]) == sorted(p[i:]):
                return "YES"
        if j < n:
            # Consider adding bj to p and incrementing j
            result = helper(i, j + 1)
            if result != "YES":
                continue

            # Check if current permutation is a valid merge of arrays a and b
            if sorted(p[:n]) == sorted(p[n:]):
                return "YES"

        memo[(i, j)] = "NO"
        return "NO"

    return helper(0, 0)
