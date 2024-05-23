def solution(name):
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    answer = 0
    idx_info = []
    
    for idx in range(len(name)):
        n =name[idx]

        # 'A'값이 아닌 정보 저장
        if n!= 'A':
            # 상하 이동값
            # 최소값(H, R)
            answer +=  min(char.find(n), len(char)-char.find(n))

            # 작업 인덱스
            idx_info.append(idx)

    # 좌우 이동값
    if len(idx_info) !=0:
        # R 이동, L이동
        if idx_info[0] ==0:
            idx_info.remove(0)

        course = [max(idx_info), len(name)-max(min(idx_info), 0)]

        # R/L 혼합 이동
        for idx in idx_info:
            if idx != max(idx_info):
                next_idx =idx_info[idx_info.index(idx)+1]
                # RR...LLLLL 이동
                course.append(idx * 2 + len(name)-next_idx)
                # LL...RRRRR 이동
                course.append((len(name)-next_idx) * 2 + idx)

        answer += min(course)
    
    
    return answer