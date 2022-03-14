def solve(board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows==0:
            return board
        cols = len(board[0])
        
        def is_border(rc):
            (rr, cc) =rc
            if rr<rows and rr< cols and rr>=0 and cc>=0 and board[rr][cc]=='O' and (rr==0 or rr==rows-1 or cc==0 or cc==cols-1):
                return True
            return False
        
        transf = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and not is_border((r,c)) and not any(map(is_border, [(r-1, c), (r+1, c), (r, c-1), (r, c+1)])):
                    transf.append((r,c))
        if transf:
            for r,c in transf:
                board[r][c]='X'
        return board

print(solve([["O","O","O"],["O","O","O"],["O","O","O"]]))