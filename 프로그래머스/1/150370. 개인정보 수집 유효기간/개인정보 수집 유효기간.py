def solution(today, terms, privacies):
    result = []
    today = int(''.join(today.split('.')))
    terms = {val.split(' ')[0]:int(val.split(' ')[1]) for val in terms}

    for idx in range(len(privacies)):
        date = privacies[idx].split(' ')[0].split('.')
        type = privacies[idx].split(' ')[1]

        # 최초 처리
        year = int(date[0]) + terms[type] // 12
        month = int(date[1]) + terms[type] % 12
        day = int(date[2]) - 1

        # 날짜 후처리
        if day == 0:
            month = month - 1
            day = 28

        # 월 후처리
        if month > 12:
            year = year + 1
            month = month - 12

        date = int(str(year) + str(month).zfill(2) + str(day).zfill(2))
        if date < today:
            result.append(idx+1)
        
    return result
    