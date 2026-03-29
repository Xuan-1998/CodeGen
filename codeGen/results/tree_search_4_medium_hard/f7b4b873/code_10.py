def find_palindromic_partitions(s):
    def is_palindrome(sub_str):
        return sub_str == sub_str[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return

        for end in range(start, len(s)):
            sub_str = s[start:end+1]
            if is_palindrome(sub_str):
                backtrack(end+1, path+[sub_str])

    result = []
    backtrack(0, [])
    return result


if __name__ == "__main__":
    s = input().strip()
    print(find_palindromic_partitions(s))
