from sys import stdin

n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()

if k <= len(s):
    # If the desired string length is less than or equal to the original string length,
    # we simply truncate the last characters if necessary.
    print(s[:k])
else:
    # If the desired string length is greater than the original string length,
    # we duplicate the original string until it reaches the desired length, then
    # remove the extra characters if there are any.
    result = s * ((k // len(s)) + (1 if k % len(s) > 0 else 0))
    print(result[:k])
