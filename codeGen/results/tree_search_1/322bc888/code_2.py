import sys

def min_operations_to_beautiful(s, queries):
    results = []
    for l, r in queries:
        # Adjust indices for 0-based indexing
        l -= 1
        r -= 1
        cost = 0
        prev_char = None
        prev_prev_char = None
        for i in range(l, r + 1):
            if s[i] == prev_char or s[i] == prev_prev_char:
                # Increment the cost if the current character is the same as the previous
                # or if it forms a palindrome with the character before the previous one
                cost += 1
                prev_prev_char = prev_char
                prev_char = None  # This character is changed, so it can be considered as None
            else:
                prev_prev_char = prev_char
                prev_char = s[i]
        results.append(cost)
    return results

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    
    results = min_operations_to_beautiful(s, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
