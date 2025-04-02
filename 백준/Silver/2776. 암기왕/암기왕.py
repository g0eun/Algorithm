t = int(input())

for i in range(t):
    n = int(input())
    note_1 = set(map(int, input().split()))   # 집합은 해시 테이블을 사용하여, 탐색에 효율적

    m = int(input())
    note_2 = map(int, input().split()) # map 객체 (이터레이터)

    for num in note_2:
        print(int(num in note_1))