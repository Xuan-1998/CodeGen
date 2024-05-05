def count_binary_numbers(n):
    memo = {}

    def f(k, i):
        if k == 0:
            return True
        binary = bin(i)[2:]
        for j in range(k - 1, len(binary) - 1):
            if binary[j] == '1' and binary[j + 1] == '1':
                return False
        return True

    def dp(k, i):
        if (k, i) in memo:
            return memo[(k, i)]
        if k > 0:
            if i % 2 == 0:
                result = dp(k - 1, i // 2)
            else:
                result = f(k, i)
        else:
            result = True
        memo[(k, i)] = result
        return result

    count = 0
    for i in range(n + 1):
        if dp(0, i):
            count += 1
    return count
