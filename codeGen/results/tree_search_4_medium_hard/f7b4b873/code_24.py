from functools import lru_cache

def partition_palindromes(s):
    @lru_cache(None)
    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    @lru_cache(None)
    def partition(i):
        if i >= len(s):
            return [[]]
        partitions = []
        for j in range(i, -1, -1):
            if is_palindrome(j, i):
                for p in partition(j-1):
                    partitions.append([s[i:j+1]] + p)
        return partitions

    return partition(len(s) - 1)

# Example usage
if __name__ == "__main__":
    s = input()
    print(partition_palindromes(s))
