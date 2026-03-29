def get_palindromic_partitions(S):
    dp = {}
    for i in range(len(S)):
        for j in range(i + 1):
            if S[j] == S[i]:
                dp[(j, i)] = True
            else:
                dp[(j, i)] = False

    partitions = []
    for i in range(len(S)):
        for j in range(i + 1):
            if dp.get((j, i), False):
                partition = [S[j:i+1]]
                for k in range(i - 1, -1, -1):
                    if S[k] == S[i]:
                        partition.insert(0, S[k:i+1])
                    else:
                        break
                partitions.append(partition)

    return list(set([tuple(p) for p in partitions]))

S = input().strip()
print(get_palindromic_partitions(S))
