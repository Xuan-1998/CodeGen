def build_failure_function(pattern):
    n = len(pattern)
    failure_function = [0] * n

    j = 1
    k = 0

    while j < n:
        if pattern[j] == pattern[k]:
            failure_function[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = failure_function[k - 1]
        else:
            j += 1

    return failure_function


def KMP_search(text, pattern):
    n = len(text)
    m = len(pattern)

    failure_function = build_failure_function(pattern)

    j = 0
    k = 0

    while j < n and k < m:
        if text[j] == pattern[k]:
            if k == m - 1:
                return True
            j += 1
            k += 1
        elif k > 0:
            k = failure_function[k - 1]
        else:
            j += 1

    return False


def check_circular(seq):
    n = len(seq)
    if n == 0:
        return "Not Circular"

    pattern = seq[1:] + seq[0]  # circular pattern
    if KMP_search(seq, pattern):
        return "Circular"
    else:
        return "Not Circular"


seq = input()
print(check_circular(seq))
