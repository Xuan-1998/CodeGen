def is_scrambled(s1, s2):
    n = len(s1)

    # Handle edge cases
    if n == 0:
        return True
    if n != len(s2):
        return False

    # Initialize memo array with False values
    memo = [[False] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        # If the result is already stored in memo, return it
        if memo[i][j]:
            return True

        # Base cases: strings of length 0 or different lengths are not scrambled
        if i == n or j == n:
            return False

        # Check if the current characters match
        if s1[i] != s2[j]:
            return False

        # Recursively check the left and right subtrees
        memo[i][j] = dfs(i + 1, j + 1)
        return memo[i][j]

    # Start the DFS from the root node (i=0, j=0)
    return dfs(0, 0)

# Example usage:
s1 = input()
s2 = input()

if is_scrambled(s1, s2):
    print("True")
else:
    print("False")
