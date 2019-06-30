class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        mem = [[-1 for _ in range(numRows)] for _ in range(numRows)]
        
        def pascal(i, j):
            if j <= 0 or j >= i:
                return 1
            if mem[i][j] == -1:
                mem[i][j] = pascal(i - 1, j - 1) + pascal(i - 1, j)
            return mem[i][j]
        
		# generate the triangle
        ptri = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = pascal(i, j)
            ptri.append(row)
			
        return ptri
        