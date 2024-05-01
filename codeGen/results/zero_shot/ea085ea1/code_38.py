def solve(str1, str2):
    trie1, trie2 = preprocess_strings(str1, str2)
    common_substrings = find_common_substrings(trie1, trie2)

    return len(common_substrings)

# Read input from stdin
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
str1 = input_stream.readline().strip()
str2 = input_stream.readline().strip()

print(solve(str1, str2))
