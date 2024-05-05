def find_max_similarity():
    n, m = map(int, input().split())
    A = input()
    B = input()

    # Initialize a dictionary to store memoized values
    dp = {}

    def lcs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        
        # Base case: When one of i or j is 0
        if i == 0 or j == 0:
            return 0
        
        # Calculate the LCS using a 1D DP approach
        if A[i-1] == B[j-1]:
            dp[(i, j)] = 1 + lcs(i-1, j-1)
        else:
            dp[(i, j)] = max(lcs(i-1, j), lcs(i, j-1))
        
        return dp[(i, j)]

    # Calculate the similarity score for each pair of substrings
    max_similarity = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            length_lcs = lcs(i, j)
            similarity = 4 * length_lcs - (i + j)
            if similarity > max_similarity:
                max_similarity = similarity
    
    print(max_similarity)

find_max_similarity()
