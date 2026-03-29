S = "a"
partitions = find_palindromic_partitions(S)
print(partitions)  # Output: ["a"]

S = "aba"
partitions = find_palindromic_partitions(S)
print(partitions)  # Output: ["aba", "ab a", "ba a", "a"]

S = "aabbaa"
partitions = find_palindromic_partitions(S)
print(partitions)  # Output: ["aabbaa", "aa bb aa", "aabb a", "a a b ba a"]
