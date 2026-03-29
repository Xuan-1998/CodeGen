def partition(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return
        for end in range(start, len(s)):
            substring = s[start:end+1]
            if is_palindrome(substring):
                backtrack(end+1, path + [substring])

    result = []
    backtrack(0, [])
    return result

def main():
    n = int(input())
    s = input().strip()
    partitions = partition(s)
    for p in partitions:
        print(' '.join(p))

if __name__ == '__main__':
    main()
