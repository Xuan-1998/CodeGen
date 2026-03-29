def min_mana_required(n, k, h):
    dp = [(0, 0, n)]
    states = sorted([(0, i+1, n) for i in range(k[0]-1)]) + dp

    for mana_usage, seconds_left, monsters_remaining in states:
        if monsters_remaining == 0:
            continue
        
        next_monster_appearance = min((k[i] - k[i-1]) for i in range(1, monsters_remaining+1))
        
        if mana_usage < next_monster_appearance:
            dp.append((mana_usage + 1, 1, monsters_remaining - 1))
        else:
            for i in range(monsters_remaining):
                if k[i] > seconds_left:
                    break
                dp.append((mana_usage + seconds_left, seconds_left, monsters_remaining - i-1))

    return dp[-1][0]
