class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows_count = len(board)
        rows_seen = {i : set() for i in range(rows_count)}
        cols_count = len(board[0])
        cols_seen = {i : set() for i in range(cols_count)}
        boxes_seen = {i : set() for i in range(int(cols_count/3))}

        for i in range(rows_count):
          current_box=0
          for j in range(cols_count):
              target = board[i][j]
              if target in cols_seen[j] or target in rows_seen[i] or target in boxes_seen[current_box]:
                return False
              if target !=".":
                rows_seen[i].add(target)
                cols_seen[j].add(target)
                boxes_seen[current_box].add(target)
              if (j+1)%3 == 0:
                current_box+=1
          if (i+1)%3==0:
            boxes_seen = {i : set() for i in range(int(cols_count/3))}
            current_box=0
        return True