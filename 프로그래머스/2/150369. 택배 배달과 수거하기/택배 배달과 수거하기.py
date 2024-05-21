def solution(cap, n, deliveries, pickups):
    
    result = 0
    
    while len(deliveries)!=0 or len(pickups)!=0:
        
        # 단위 작업 <시작>
        work_list = []
        
        for work in [deliveries, pickups]:
            cnt = cap
            maxlen = len(work)
            for idx in range(maxlen, 0, -1):
                # -- 비대상건
                if work[idx - 1] == 0:
                    del work[idx - 1]
                
                # -- 대상건
                else:
                    work_list.append(idx)                    
                    # 1) 진행중
                    if cnt > work[idx - 1]:
                        cnt = cnt - work[idx - 1]
                        del work[idx - 1]
                    
                    # 2) 완료
                    else:
                        # 재방문 O
                        if work[idx - 1] > cnt:
                            work[idx - 1] = work[idx - 1] - cnt
                        # 재방문 X
                        else:
                            del work[idx - 1]

                        # <종료>
                        break

        # 왕복 거리(거리가 먼 작업 기준)
        if len(work_list)>0:
            result += max(work_list)*2
        
    return result