def generate_palindrome(n):
    palindrome = [i for i in range(1, n // 2 + 1)]
    if n % 2 == 0:
        return palindrome + list(reversed(palindrome))
    else:
        return palindrome + [n] + list(reversed(palindrome))

def recursive_sort(arr, x):
    # Your original sorting function implementation goes here
    pass

def main():
    n = int(input())
    permutation = generate_palindrome(n)
    print(" ".join(map(str, permutation)))

if __name__ == "__main__":
    main()
