def partition_palindromes(s):
    memo = {}

    def is_palindrome(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        substring = s[i:j+1]
        if substring == substring[::-1]:
            return True
        else:
            return False

    result = []

    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(i, j):
                partition = [s[i:j+1]]
                memo[(i, j)] = True
                recursive_partition(i, j, partition)
                result.append(partition)

    return result


def recursive_partition(i, j, partition):
    for k in range(i, j+1):
        if is_palindrome(i, k) and is_palindrome(k+1, j):
            new_partition = partition + [s[i:k+1], s[k+1:j+1]]
            memo[(i, j)] = True
            recursive_partition(k+1, j, new_partition)


if __name__ == "__main__":
    s = input()
    print(partition_palindromes(s))
