def all_palindrome_partitions(S):
    memo = {}

    def recurse(S, partition, memo):
        if len(S) == 0:  # Base case: when the remaining string is empty
            return [partition]

        result = []
        for i in range(len(S)):
            prefix = S[:i+1]
            suffix = S[i+1:]
            if prefix == prefix[::-1]:  # If the prefix is a palindrome
                partitions = recurse(suffix, partition + [prefix], memo)
                result.extend(partitions)

        return result

    return recurse(S, [], memo)[0]

# Test the function
S = input()
print(all_palindrome_partitions(S))
