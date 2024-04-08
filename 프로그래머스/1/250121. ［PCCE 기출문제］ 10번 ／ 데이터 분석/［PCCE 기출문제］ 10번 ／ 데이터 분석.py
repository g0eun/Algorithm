def solution(data, ext, val_ext, sort_by):
    # 데이터 정보
    fld = ['code', 'date', 'maximum', 'remain']
    ext_idx = fld.index(ext)
    sort_idx = fld.index(sort_by)
    
    # 대상 필드 기준 추출/정렬    
    answer = [x for x in data if x[ext_idx]<val_ext]
    answer.sort(key=lambda x:x[sort_idx])
    

    return answer