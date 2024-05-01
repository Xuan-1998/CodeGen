def subset_sums():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Sort the array in increasing order
    arr.sort()

    sums = set()
    for i in range(2 ** n):
        total_sum = 0
        for j in range(n):
            if (i & (1 << j)):
                total_sum += arr[j]
        sums.add(total_sum)

    print(' '.join(map(str, sorted(list(sums)))))

subset_sums()
