class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matxix[0])

        total = n * m
        ans = []
        c = 0

        col_start = 0
        col_end = m - 1
        row_start = 0
        row_end = n - 1

        while c < total:
            for i  in range(col_start, col_end + 1):
                ans.append(matrix[row_start][i])
                c += 1
            row_start += 1

            if c == total:
                break

            for i in range(row_start, row_end + 1):
                ans.append(matrix[i][col_end])
                c += 1
            col_end -= 1

            if c == total:
                break
            
            for i in range(col_end, col_start -1, -1):
                ans.append(matrix[row_end][i])
                c += 1
            row_end -= 1

            if c == total:
                break

            for i in range(row_end, row_start -1, -1):
                ans.append(matrix[i][col_start])
                c += 1
            col_start += 1
            
        return ans