from math import gcd
def find_winner(M, X):
    winners = []
    for i in range(1, X+1):
        temp_winners = set()
        people_left = i
        removed_index = 0
        while people_left > 1:
            removed_index = (removed_index + M - 1) % people_left
            people_left -= 1
            if removed_index == 0:
                temp_winners.add(1)
            else:
                temp_winners.add(removed_index+1)
        winners.append(sorted(list(temp_winners))[-1])
    return winners

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    print(*find_winner(M, X))
