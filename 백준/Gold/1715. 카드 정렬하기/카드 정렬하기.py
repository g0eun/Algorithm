import heapq

# 입력값 처리
n = int(input())
total_cnt = [int(input()) for _ in range(n)]

# 초기값
result = 0

# 리스트를 최소 힙으로 변환
heapq.heapify(total_cnt)

while len(total_cnt) > 1:
    # 최소묶음 2개 비교
    chk = heapq.heappop(total_cnt) + heapq.heappop(total_cnt)

    # 내역 업데이트
    heapq.heappush(total_cnt, chk)
    result+=chk

print(result)