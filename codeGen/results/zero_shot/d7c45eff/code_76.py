# Take input
n, k = map(int, input().split())
s = input()

if k >= n:
    # If length of string is equal or more than desired length, duplicate string
    print(s * (k // n))
else:
    # If length of string is less than desired length, delete last character and repeat if necessary
    print(s[:k])
