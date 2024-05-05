def partition_palindromes(s):
    dp = {(i, []): [[(s[:i+1])[::-1] + s[i+1:]]] for i in range(len(s))}

    for length in range(2, len(s) + 1):
        for i in range(len(s) - length + 1):
            if (s[i:i+length])[::-1] == s[i:i+length]:
                for p in dp.get((i-1, []), []):
                    dp[(i, [])].extend([p + [(s[i:i+length])] + r for r in dp.get((len(s)-length-i-1, p + [(s[i:i+length])]), [])])

    return dp.get((0, []), [[]])[0]

print(partition_palindromes(input()))
