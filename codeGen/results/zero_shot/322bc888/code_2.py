def min_operations_to_beautiful(n, m, s, queries):
    results = []
    for l, r in queries:
        # We will iterate over the substring and apply the greedy approach.
        operations = 0
        i = l - 1  # Convert to 0-based index
        while i < r - 1:  # r - 1 because we look ahead by one character
            if s[i] == s[i + 1]:
                # We found a palindrome of length 2, change the next character
                operations += 1
                # Skip the next character as we've changed it
                i += 2
            elif i + 2 < r and s[i] == s[i + 2]:
                # We found a palindrome of length 3, change the middle character
                operations += 1
                # Skip the next character as we've changed it
                i += 3
            else:
                # No palindrome, move to the next character
                i += 1
        results.append(operations)
    return results

# Read input from stdin and output the result to stdout
if __name__ == "__main__":
    n, m = map(int, input().split())
    s = input()
    queries = [tuple(map(int, input().split())) for _ in range(m)]
    results = min_operations_to_beautiful(n, m, s, queries)
    for res in results:
        print(res)
