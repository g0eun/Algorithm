n = int(input())
meetings = [tuple(map(int, input().split())) for i in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

cnt=0
final_end = 0

for start, end in meetings:
    if start >= final_end:
        cnt += 1
        final_end = end

print(cnt)