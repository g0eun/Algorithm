def solution(bandage, health, attacks):
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    attacks.insert(0, [0,0])
    
    # 초기 체력
    hp = health

    for idx in range(len(attacks)-1):
        # 직전 공격, 현재 공격
        a0 = attacks[idx]
        a1 = attacks[idx+1]
        
        # 공격 이후 체력 계산
        opt_time = a1[0] - a0[0] - 1
        hp = min(hp + opt_time * x + opt_time//t * y, health)
        hp = hp - a1[1]

        if hp <= 0:
            return -1
        
    return hp