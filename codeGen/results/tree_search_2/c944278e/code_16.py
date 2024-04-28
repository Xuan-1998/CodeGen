def winning_teams(n, s):
    if n == 0:
        return [set()]
    else:
        result = []
        for i in range(2**n):
            bit_mask = (1 << (n-1))
            while bit_mask > 0:
                team_idx = (i & bit_mask) >> (n-1)
                if s[team_idx] == '1':
                    result.append({i})
                bit_mask >>= 1
        return result

def print_winning_teams(n, s):
    winning_teams_set = set()
    for i in range(2**n):
        team_idx = i ^ (i >> 1)
        if s[team_idx] == '1':
            winning_teams_set.add(i)
    winning_teams_list = list(winning_teams_set)
    winning_teams_list.sort()
    print(*winning_teams_list, sep='\n')

# Example usage
n = int(input())
s = input()
print_winning_teams(n, s)
