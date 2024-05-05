def partition_palindromes(S):
    def recurse(i, S, partition):
        if i >= len(S):
            return [partition]
        
        current_char = S[i]
        new_partition = partition + [current_char]  # add the current character to the palindromic partition
        
        if i > 0 and current_char == S[i-1]:
            new_partition = partition
        else:
            for j in range(i):
                state = (j, S[j:i+1], [])  # create a state tuple
                if S[j:i+1] == S[j:i+1][::-1]:  # check if the substring is a palindrome
                    memoization[state] = [(state[2] + [S[j:i+1]])]
                else:
                    for p in memoization.get((i, S[i+1:], []), [[]]):
                        memoization.setdefault(state, []).extend([p + [S[j:i+1]]])
        
        return memoization[(0, S, [])].pop(0)  # remove the base case
        
    memoization = {}
    result = recurse(len(S)-1, S, [])
    
    for partition in result:
        print(' '.join(partition))  # print each palindromic partition

if __name__ == "__main__":
    S = input()
    partition_palindromes(S)
