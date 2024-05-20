def solution(s):
    result = []
    maxlen = len(s)
    
    if maxlen ==1:
        result = [1]
    
    else:
        # 문자열 단위 길이
        for length in range(maxlen // 2, 0, -1):
            idx = 0
            text = ''
            while idx < maxlen:
                token = s[idx: min(idx + length, maxlen)]
                cnt = 1

                # 토큰 반복 횟수
                while s[idx + cnt * length:].find(token) == 0:
                    cnt += 1

                # 결과값 저장
                if cnt == 1:
                    text += f"{token}"
                else:
                    text += f"{cnt}{token}"

                # 다음 확인 구간
                idx = idx + cnt * length

            result.append(len(text))

    return min(result)

