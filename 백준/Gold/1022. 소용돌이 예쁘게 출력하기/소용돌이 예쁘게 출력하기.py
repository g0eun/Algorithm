# 입력값 처리
r1, c1, r2, c2 = map(int, input().split())

matrix = []
for r in range(r1, r2 + 1):
    row = []
    for c in range(c1, c2 +1):
        lv = max(abs(r), abs(c)) # 레벨
        lv_max = (2*lv + 1) ** 2 # 레벨 최대값

        # 시계 방향으로 감소
        if r == lv: # ←
            num = lv_max - (lv-c)
        elif c == -lv: # ↑
            num = lv_max - 2*lv - (lv-r)
        elif r == -lv: # →
            num = lv_max - 2 * lv *2 - (c+lv)
        elif c == lv: # ↓
            num = lv_max - 2 * lv * 3 - (r+lv)

        row.append(num)

    matrix.append(row)

# 출력 글자수 (최대값 기준)
digit = len(str(max(map(lambda x: max(x), matrix))))

# 결과 출력
for row in matrix:
    print(' '.join(map(lambda x: str(x).rjust(digit), row)))