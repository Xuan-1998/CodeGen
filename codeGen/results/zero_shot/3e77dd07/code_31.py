import itertools

def is_scrambled(s1, s2):
    if len(s1) != len(s2):
        return False
    
    # Generate all possible binary tree partitions of s1
    def partition_string(s):
        if len(s) == 0:
            return [""]
        result = []
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            for p_left, p_right in itertools.product(partition_string(left), partition_string(right)):
                result.append(p_left + right + p_right)
        return result
    
    # Check if any permutation of the binary tree partitions matches s2
    for p in partition_string(s1):
        if p == s2:
            return True
    
    return False

s1 = input()
s2 = input()

if is_scrambled(s1, s2):
    print("True")
else:
    print("False")
