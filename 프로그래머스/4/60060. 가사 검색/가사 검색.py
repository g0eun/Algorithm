from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(words, queries):

    # 단어 글자수 정방향/역방향 저장
    word_dict = defaultdict(list)
    reversed_word_dict = defaultdict(list)

    for word in words:
        word_dict[len(word)].append(word)
        reversed_word_dict[len(word)].append(word[::-1])


    # 정렬
    for length in word_dict:
        word_dict[length].sort()
        reversed_word_dict[length].sort()


    # 결과 카운트
    answer = []
    for q in queries:
        if q[0]!='?': # 접두사 쿼리 (fro??)
            left = bisect_left(word_dict[len(q)], q.replace('?', 'a'))
            right = bisect_right(word_dict[len(q)], q.replace('?', 'z'))
        else: # 접미사 쿼리 (???o)
            reversed_q = q[::-1]
            left = bisect_left(reversed_word_dict[len(q)], reversed_q.replace('?', 'a'))
            right = bisect_right(reversed_word_dict[len(q)], reversed_q.replace('?', 'z'))

        answer.append(right-left)

    return answer