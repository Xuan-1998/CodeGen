def can_send_b(b):
    memo = {}

    def is_possible(i, p):
        if (i, p) in memo:
            return memo[(i, p)]

        if i == len(b):
            return True

        for j in range(1, min(len(p), 10**9) + 1):  # adjust the max segment length
            if p[:j] == str(j) * j:  # check if the current segment matches the prefix
                result = is_possible(i + j, p[j:])
                memo[(i, p)] = result
                return result

        return False

    return "YES" if is_possible(0, "") else "NO"
