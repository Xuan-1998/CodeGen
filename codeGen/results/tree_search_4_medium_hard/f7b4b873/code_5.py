def partition_palindromes(S):
    def is_palindrome(s):
        return s == s[::-1]

    memo = {}
    result = []

    def dfs(i, partition):
        if (i, partition) in memo:
            return memo[(i, partition)]
        
        if i >= len(S):
            result.append(partition)
            return [partition]
        
        partitions = []
        for c in range(i, len(S)):
            if is_palindrome(S[i:c+1]):
                partitions.extend(dfs(c+1, partition + [S[i:c+1]]))
        
        memo[(i, partition)] = partitions
        return partitions

    dfs(0, [])
    return result

def main():
    S = input()
    print(partition_palindromes(S))

if __name__ == "__main__":
    main()

