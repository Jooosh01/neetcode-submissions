class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix)-1
        while t <= b:
            m = (t+b)//2
            if target >= matrix[m][0] and target < matrix[m+1][0]:
                row  = matrix[m]
                l, r  = 0, len(row)-1
                while l <= r:
                    i = (l+r)//2
                    if row[i] > target:
                        r = i -1
                    elif row[i] < target:
                        l = i +1
                    else:
                        return True
            elif matrix[m][0] > target:
                b = m-1
            else:
                t = m +1   
        return False     
