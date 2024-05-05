import sys

def ladder_query(array, queries):
    n = len(array)
    m = len(queries)

    decreasing = []
    increasing = []

    for query in queries:
        l, r = query
        subarray = array[l-1:r]
        
        for i in range(len(subarray)-1, -1, -1):
            if subarray[i] <= subarray[i-1]:
                decreasing.append(subarray[i])
            else:
                increasing.append(subarray[i])

        ladder = False
        for i in range(len(decreasing)):
            for j in range(len(increasing)):
                if set(decreasing[:i]) == set(subarray[:l-1]) and set(increasing[:j]) == set(subarray[l:r]):
                    ladder = True
                    break

            if ladder:
                break

        print("Yes" if ladder else "No")
