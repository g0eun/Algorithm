def solution(friends, gifts):
    
    gifts = [value.split(' ') for value in gifts]
    
    result=[]
    for from_name in friends:
        count = 0
        for to_name in [name for name in friends if name!=from_name]:
            # 1) 두 사람 사이에 더 많은 선물을 준 사람 
            from_cnt = gifts.count([from_name,to_name])
            to_cnt = gifts.count([to_name,from_name])
            if from_cnt > to_cnt:
                count = count + 1
            # 2) 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면 
            elif from_cnt == to_cnt:
                from_name_point = sum([value[0]==from_name for value in gifts]) - sum([value[1]==from_name for value in gifts])
                to_name_point = sum([value[0] == to_name for value in gifts]) - sum([value[1] == to_name for value in gifts])
                # 선물 지수가 더 큰 사람 
                if from_name_point > to_name_point:
                    count = count + 1
                
        result.append(count)
        
    answer = max(result)
    
    return answer

