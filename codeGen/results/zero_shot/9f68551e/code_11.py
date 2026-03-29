import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        k = list(map(int, sys.stdin.readline().split()))
        h = list(map(int, sys.stdin.readline().split()))
        
        # Initialize the damage and mana
        damage = 1
        mana = 0
        
        # Iterate over each monster
        for i in range(n):
            while k[i] > 0:
                # If we didn't cast a spell at the previous second
                if k[i] != k[i-1]:
                    damage += 1
                # If we can kill the monster with the current damage, do so
                if damage >= h[i]:
                    mana += damage
                    break
                # Otherwise, increment the time and try again
                k[i] -= 1
            else:
                # If we didn't cast a spell at the previous second and couldn't kill the monster, increment the time
                k[i] = 0
        
        print(mana)

if __name__ == "__main__":
    solve()
