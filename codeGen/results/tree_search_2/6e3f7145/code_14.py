def longest_palindromic_substring(s):
    s = '#' + '#'.join(s) + '#'
    n = len(s)
    P = [0] * n
    C = R = 0

    for i in range(1, n - 1):
        if R > i:
            i_mirror = 2*C-i
            P[i] = min(P[i_mirror], R-i)

        else:
            P[i] = 0

        while s[i + 1 + P[i]] == s[i - 1 - P[i]]:
            P[i] += 1

        if i + P[i] > R:
            C, R = i, i + P[i]

    maxLen, centerIndex = max((n, i) for i,n in enumerate(P))
    return s[centerIndex-maxLen: centerIndex+maxLen].replace('#', '')

def main():
    s = input()
    print(longest_palindromic_substring(s))

if __name__ == "__main__":
    main()

