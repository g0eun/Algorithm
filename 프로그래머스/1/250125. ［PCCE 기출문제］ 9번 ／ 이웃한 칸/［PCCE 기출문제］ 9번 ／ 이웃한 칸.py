def solution(board, h, w):
    # 보드 사이즈
    n = len(board)
    
    # 확인 좌표 정보(delta)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    count =0 
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        # 색상 체크
        if (0 <= h_check < n) and (0 <= w_check < n):
            if board[h][w] == board[h_check][w_check]:
                count+=1

    return count