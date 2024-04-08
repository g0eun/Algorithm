def solution(n, words):
    
    # 끝말잇기 조건 체크
    answer = []
    
    for idx in range(0, len(words)):
        cond1 = len(words[idx])==1
        cond2 = words[idx-1][-1]!=words[idx][0]
        cond3 = words[idx] in words[:idx]
        
        # -- 탈락
        if idx == 0 and cond1:
            break
        elif idx !=0 and any([cond1, cond2, cond3]):
            break
        # -- 성공
        else:
            if idx == len(words)-1:
                answer = [0,0]

    # 출력값 처리
    if len(answer)==0:
        answer = (idx%n + 1, idx//n + 1)

    return answer