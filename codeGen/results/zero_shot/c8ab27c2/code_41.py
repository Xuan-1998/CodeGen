s = input()
t = input()
subsequence_length = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        subseq = s[i:j]
        if not is_subsequence(subseq, t):
            return j - i
def is_subsequence(sub, seq):
    sub_index = 0
    for char in seq:
        while sub_index < len(sub) and char != sub[sub_index]:
            sub_index += 1
        if sub_index == len(sub):
            return False
        sub_index += 1
    return True
