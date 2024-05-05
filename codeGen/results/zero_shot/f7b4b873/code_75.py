def palindromic_partitions(S):
    def expand_around_center(s, left, right):
        while left <= right and s[left] == s[right]:
            left += 1
            right -= 1
        return s[left:right+1]

    partitions = [[]]
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            partition = S[:i] + [S[i:j]]
            if all(partition[k].lower() == partition[k][::-1].lower() for k in range(len(partition))):
                partitions.append(partition)

    return partitions

if __name__ == "__main__":
    S = input()
    print(palindromic_partitions(S))
