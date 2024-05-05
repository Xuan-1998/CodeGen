def palindromic_partitions(s):
    def expand_around_center(left, right):
        while left <= right and s[left] == s[right]:
            left += 1
            right -= 1

        return s[left:right+1]

    partitions = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            partition = expand_around_center(i, j - 1)
            if partition:
                partitions.append([partition])

    return partitions

s = input()
print(palindromic_partitions(s))
