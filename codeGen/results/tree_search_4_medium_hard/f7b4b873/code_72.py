def is_palindrome(s):
    return s == s[::-1]

def partition_palindromes(S):
    def helper(state, partitions):
        if len(state) > 0:
            for i in range(len(S) - len(state), -1, -1):
                new_state = S[:i] + state
                if is_palindrome(new_state):
                    partitions.append(partitions[:])
                    helper((new_state[len(state):],), [partitions[-1] + [new_state]])
        else:
            if is_palindrome(S):
                partitions.append([S])
            for i in range(len(S) - 1, -1, -1):
                new_state = S[:i+1]
                if is_palindrome(new_state):
                    partitions.append(partitions[:])
                    helper((new_state[1:],), [partitions[-1] + [new_state]])
        return partitions

    max_len = len(S)
    return helper("", [[]])

def print_partitions(partitions):
    for i, partition in enumerate(partitions):
        print(f"Partition {i+1}: {partition}")

S = input()
partitions = partition_palindromes(S)
print_partitions(partitions)
