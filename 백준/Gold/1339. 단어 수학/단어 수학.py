# # 입력값 처리
n = int(input())
word_list = [str(input()) for _ in range(n)]

# 사용 문자열
char_list = {char:0 for char in set(''.join(word_list))}

for word in word_list:
    # 지수 초기화
    idx=0
    for char in reversed(word):
        # 문자열 자릿값 업데이트 (합산)
        char_list[char] += 10**idx
        idx+=1

# 최대값부터 정렬
chk_list = sorted(char_list.values(), reverse=True)

# 최종 결과
char_num = 9
result = 0
for chk in chk_list:
    result += char_num * chk
    char_num-= 1

print(result)