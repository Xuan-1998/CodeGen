def min_operations_to_beautiful(substring):
    operations = 0
    i = 0
    while i < len(substring) - 1:
        # Check for two consecutive characters that are the same
        if substring[i] == substring[i + 1]:
            operations += 1
            i += 2  # Skip the next character as it's already been made non-palindromic
        # Check for a palindromic triplet
        elif i < len(substring) - 2 and substring[i] == substring[i + 2]:
            operations += 1
            i += 3  # Skip the next two characters as they've been made non-palindromic
        else:
            i += 1
    return operations

def main():
    n, m = map(int, input().split())
    s = input()
    for _ in range(m):
        l, r = map(int, input().split())
        # Adjust indices since the input is 1-based and Python uses 0-based indexing
        result = min_operations_to_beautiful(s[l - 1:r])
        print(result)

if __name__ == "__main__":
    main()
