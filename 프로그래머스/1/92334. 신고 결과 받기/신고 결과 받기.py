def solution(id_list, report, k):
    
    # ID 별 결과 요약
    user_report = {id :[] for id in id_list}
    summary = {id :0 for id in id_list}

    # 유저ID, 신고 ID
    for val in set(report):
        user_id, report_id = val.split(" ")
        user_report[user_id].append(report_id)
        summary[report_id] +=1

    # 정지된 ID
    block_list = dict(filter(lambda x: x[1]>=k, summary.items())).keys()

    # 처리 결과 메일 건수
    result = [len(set(block_list)&set(val[1])) for val in user_report.items()]

    return result