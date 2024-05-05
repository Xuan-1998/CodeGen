def partition_palindromic(S):
    memo = {}
    def is_palindrome(s):
        return s == s[::-1]

    def dfs(i, S, partition):
        if i >= len(S):
            return [partition]
        if (i, S[:i+1]) in memo:
            return memo[(i, S[:i+1])] 
        partitions = []
        for j in range(i, -1, -1):
            if is_palindrome(S[j:i+1]):
                partitions.extend(dfs(j-1, S[:j], partition + [S[j:i+1]]))
        memo[(i, S[:i+1])] = partitions
        return partitions

    result = dfs(len(S)-1, S, [])
    return result

def main():
    N = int(input())
    S = input()
    result = partition_palindromic(S)
    for partition in result:
        print(partition)

if __name__ == "__main__":
    main()
