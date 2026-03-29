from sys import stdin

def is_palindrome(s):
    return s == s[::-1]

def find_partitions(s):
    n = len(s)
    partitions = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                partition = [substr]
                k = i - 1
                while k >= 0 and s[k] == s[n - j]:
                    partition.append(s[:k+1])
                    k -= 1
                if k < 0:
                    partitions.append(partition)
    return partitions

def main():
    s = stdin.readline().strip()
    result = find_partitions(s)
    for p in result:
        print(' '.join(p))

if __name__ == "__main__":
    main()
