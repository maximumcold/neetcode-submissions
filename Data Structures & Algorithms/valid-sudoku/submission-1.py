class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        s   = [set() for i in range(9)]

        for i, r in enumerate(board):

            for j, value in enumerate(r):
                if value == ".":
                    continue
                box_index = (i // 3) * 3 + (j // 3)    
                if value in col[i] or value in row[j] or value in s[box_index]:
                    return False

                col[i].add(value)
                row[j].add(value)

                s[box_index].add(value)

        return True
