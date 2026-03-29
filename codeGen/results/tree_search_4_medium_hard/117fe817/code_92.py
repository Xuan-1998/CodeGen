def find_count(n):
    memo = {0: 0}

    def helper(k):
        if k not in memo:
            last_bit = (1 << k) - 1
            if last_bit > n:
                result = 0
            else:
                ones = helper(k - 1)
                result = ones * (last_bit + 1)
            if k % 2 == 1:
                result += ones
            memo[k] = result
        return memo[k]

    return helper(int(math.log2(n)).bit_length())

if __name__ == "__main__":
    n = int(input())
    print(find_count(n))
