def partition_palindromic(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    def recursive_partition(index, current_partition):
        if index >= len(s):
            result.append(current_partition[:])
            return
        for i in range(index + 1, len(s) + 1):
            substring = s[index:i]
            if is_palindrome(substring):
                recursive_partition(i, current_partition + [substring])

    result = []
    recursive_partition(0, [])
    return result

if __name__ == "__main__":
    N = int(input())  # Read the length of the input string
    S = input()  # Read the input string
    print(partition_palindromic(S))
