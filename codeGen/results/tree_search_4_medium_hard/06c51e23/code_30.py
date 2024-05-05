import sys

# Memoization decorator
def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func

@memoize
def round_up_to_i(digits_after_decimal):
    # Your logic to compute the maximum possible grade goes here
    pass

@memoize
def dp(i, digits_after_decimal):
    if i == 0:
        return 1
    return max(dp(i-1), round_up_to_i(digits_after_decimal[:i]))

n, t = map(int, input().split())
fraction = float(input())

# Convert the fraction to a string with the desired precision
precision = len(str(fraction).split('.')[1])
digits_after_decimal = str(fraction).split('.')[1]

print(dp(precision, digits_after_decimal))
