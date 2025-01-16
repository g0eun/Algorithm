# 입력값 처리
n = int(input())
ai = list(map(int,input().split()))

# 입력값 정렬
ai.sort()

# GOOD 검증
result = 0
for idx, a in enumerate(ai):

    left, right =0, n-1


    while left < right:

        # 왼/오 한칸씩 이동하며 검등 (단, 현재 idx 제외)
        if left == idx:
            left += 1
            continue

        if right == idx:
            right -= 1
            continue

        # 합계값
        current_sum = ai[left] + ai[right]

        if current_sum == a:
            result += 1
            break
        elif current_sum < a:
            left += 1
        else:
            right-= 1


# 결과값 출력
print(result)