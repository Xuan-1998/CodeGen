import sys
from collections import defaultdict

def main():
    test_cases = int(sys.stdin.readline())
    
    for _ in range(test_cases):
        n = int(sys.stdin.readline())  # Number of monsters
        
        monster_times = list(map(int, sys.stdin.readline().split()))
        monster_healths = list(map(int, sys.stdin.readline().split()))
        
        monster_dict = defaultdict(list)
        for i in range(n):
            monster_dict[monster_times[i]].append(monster_healths[i])
        
        mana_required = 0
        prev_mana = 0
        
        for time, health in sorted(monster_dict.items()):
            while monster_dict[time]:
                health_to_kill = max(monster_dict[time])
                if prev_mana + health > health_to_kill:
                    mana_required += prev_mana + health - health_to_kill
                else:
                    mana_required += 1
                prev_mana = health_to_kill
                monster_dict[time].pop(0)
        
        print(mana_required)

if __name__ == "__main__":
    main()
