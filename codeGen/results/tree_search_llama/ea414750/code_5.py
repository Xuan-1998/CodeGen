def count_bear_pairs(s):
    n = len(s)
    z_function = [0] * (n + 1)

    for i in range(n):
        if s[i] == 'b':
            j = i + 1
            while j <= n and s[j] == 'e' or s[j] == 'r':
                j += 1
            z_function[i + 1:j] = [j - i - 1] * (j - i)

    count = 0
    for i in range(n):
        if s[i:i+4] == 'bear':
            count += 1

    return count

if __name__ == "__main__":
    s = input()
    print(count_bear_pairs(s))
