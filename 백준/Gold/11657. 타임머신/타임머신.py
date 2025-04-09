# 입력값 처리
n, m = map(int, input().split())
edge_list = [tuple(map(int, input().split())) for _ in range(m)]

# 무한대 상수 정의
INF = int(1e9)

# 거리 초기화
distance = [INF] * n
distance[0] = 0

# 반복 작업
updated = False
for _ in range(n-1):
    for start, end, dist in edge_list:
        if distance[start-1] != INF and distance[end-1] > distance[start-1] + dist:
            distance[end-1] = distance[start-1] + dist
            updated = True

    if not updated:
        break

# 음수 사이클 확인
negative_cycle = False
for start, end, dist in edge_list:
    if distance[start-1]!=INF and distance[end-1] > distance[start-1]+dist:
        negative_cycle = True
        break


# 결과 출력
if negative_cycle:
    print(-1)
else:
    for dist in distance[1:]:
        print(-1 if dist == INF else dist)