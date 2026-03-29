def count_good_subsequences(a, i, b):
    if i >= len(a):  
        return 1 if b else 0  

    good_subseqs = 0
    for j in range(i+1, len(a)+1):  
        if all(k % (k-1) == 0 for k in b + [a[j]]):  
            good_subseqs += count_good_subsequences(a, j, b + [a[j]])

    return good_subseqs

def main():
    n = int(input())  
    a = [int(x) for x in input().split()]  

    good_subseqs = 0
    for i in range(1, n+1):  
        good_subseqs += count_good_subsequences(a, i, [a[0]])

    print(good_subseqs % (10**9 + 7))  

if __name__ == "__main__":
    main()
