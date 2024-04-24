# 입력값 설정
N = int(input())


# 페스티벌 정보
# info :  [[등수, 상금, 누적 인원], ...]
a_info =  [[1, 5000000, 1],[2, 3000000, 2], [3, 2000000, 3], [4, 500000, 4], [5, 300000, 5], [6, 100000, 6]]
for i in range(1, len(a_info)):
    a_info[i][2] = a_info[i-1][2] + a_info[i][2]

b_info = [[1, 5120000, 1],[2, 2560000, 2], [3, 1280000, 4], [4, 640000, 8], [5, 320000, 16]]
for i in range(1, len(b_info)):
    b_info[i][2] = b_info[i-1][2] + b_info[i][2]


# 상금 계산
for i in range(N):
    
    a,b = map(int,input().split())
    
    prize = 0

    # 상금 획득 인원 내, 계산
    if 1<= a <= a_info[-1][2]:
        for info in a_info:
            if info[2]>= a:
                prize += info[1]
                break

    if 1<= b <= b_info[-1][2]:
        for info in b_info:
            if info[2]>= b:
                prize += info[1]
                break

    print(prize)