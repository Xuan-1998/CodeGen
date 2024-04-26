def count_bear_substrings():
    s = input().strip()

    count = 0
    for i in range(len(s)):
        for j in range(i + 4):  # 'bear' has 4 characters, so we only need to consider pairs (i, j) where j - i <= 3
            substring = s[i:j+1]
            if substring == 'bear':
                count += 1

    print(count)

count_bear_substrings()
