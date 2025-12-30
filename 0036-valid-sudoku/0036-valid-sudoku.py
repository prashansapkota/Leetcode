from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we have to count char in list. so we count the occurance of each character in nested list and keep count of each number in the list. if the char occurs more than once we return false otherwise we check the character on the running char of the list for all. and we only check if the value there is number otherwise we do nothing. 
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r // 3, c // 3]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])

        return True


        