def max_beauty(arr, bad_primes):
    max_beauty = 0
    for _ in range(len(arr)):
        arr = perform_operation(arr)
        beauty = f(arr)
        if beauty > max_beauty:
            max_beauty = beauty
    return max_beauty

def f(s):
    # implement this part later
    pass
