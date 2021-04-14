class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:\

        def generate():
            board = []
            for i in range(n):
                row[quene[i]] = "Q"
                board.append("".join(row))
                row[quene[i]] = "."
            return board
        
        def backtrack(m, n, columns, diag1, diag2, res):
            if m == n:
                temp = generate()
                res.append(temp)
            
            for i in range(n):
                if i not in columns and m+i not in diag1 and m-i not in diag2:
                    quene[m] = i
                    columns.add(i)
                    diag1.add(m+i)
                    diag2.add(m-i)

                    backtrack(m+1, n, columns, diag1, diag2, res)
                    columns.remove(i)
                    diag1.remove(m+i)
                    diag2.remove(m-i)
        res = []
        columns = set()
        diag1 = set()
        diag2 = set()
        row = ["."] * n
        quene = [0] * n
        m = 0
        backtrack(m, n, columns, diag1, diag2, res)
        return res