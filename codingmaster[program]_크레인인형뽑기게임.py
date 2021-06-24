def solution(board, moves):
    answer = 0
    stack = []

    for m in moves:
        m -= 1
        i = 0
        while board[i][m] == 0:
            i += 1
            if i >= len(board):
                i -= 1
                break
        
        doll = board[i][m]
        if doll == 0:
            continue

        board[i][m] = 0

        if not stack:
            stack.append(doll)
        elif (stack[-1] - doll) == 0:
            answer += 1
            stack.pop()
            while (stack[-1] - doll) == 0:
                answer += 1
                stack.pop()
        else:
            stack.append(doll)

    return answer * 2


A = [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
a = solution(A, moves)
a
