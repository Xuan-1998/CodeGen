def partition_palindromes(s):
    memo = {}

    def helper(last_char, remaining_str):
        if (last_char, remaining_str) in memo:
            return memo[(last_char, remaining_str)]

        result = []
        if remaining_str == "":
            result.append([""])
        else:
            for i in range(len(remaining_str)):
                prefix = remaining_str[:i+1]
                suffix = remaining_str[i+1:]
                if prefix == prefix[::-1]:
                    result.extend([list(x) + [prefix] for x in helper(prefix[-1], suffix)])
            memo[(last_char, remaining_str)] = result
        return result

    result = []
    partitions = helper("", s)
    for partition in partitions:
        result.append(["".join(x) for x in partition])

    return result


if __name__ == "__main__":
    N = int(input())
    S = input().strip()
    print(partition_palindromes(S))
