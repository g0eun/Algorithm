from collections import defaultdict
import heapq


# 입력값 처리
n, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 경로 경우의 수 ( 1 > v1 > v2 > N / 1 > v2> v1 > N)
total_case = [[(1, v1), (v1, v2), (v2, n)], [(1, v2), (v2, v1), (v1, n)]]
min_distance = float("inf")

for route in total_case:

    valid_route = True
    route_distance =0

    for start, end in route:
        # 거리 정보 초기화
        distances = [float("inf")] * (n + 1)
        distances[start] = 0 # 시작점 0
        priority_queue = [(0, start)] # (거리, 정점)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # queue 입력 거리가 dist 보다 크다면 무시
            if current_distance > distances[current_node]:
                continue

            # 현재 노드의 인접 정보 확인
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight

                # 더 짧은 경로 있다면 갱신
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        if distances[end] == float("inf"):
            valid_route = False
            break

        route_distance += distances[end]

    if valid_route:
        min_distance = min(min_distance, route_distance)


# 결과 출력
print(min_distance if min_distance != float("inf") else -1)