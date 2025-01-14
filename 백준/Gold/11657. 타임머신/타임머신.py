# 입력값 처리
n, m = map(int, input().split())
route_list = [list(map(int, input().split())) for _ in range(m)]

# 초기값
distance = [float("inf")] * n
distance[0] = 0  # 1번 도시의 초기 거리

# 간선 완화 (n-1 번)
for i in range(n):
    update = False

    for start, end, dist in route_list:
        if distance[start - 1] != float("inf") and distance[end - 1] > distance[start - 1] + dist:
            distance[end - 1] = distance[start - 1] + dist
            update = True

    # 음수 사이클 검증
    if i == n - 1 and update:
        print(-1)
        exit()

# 결과 출력
for i in range(1, n):
    if distance[i] == float("inf"):
        print(-1)
    else:
        print(distance[i])
