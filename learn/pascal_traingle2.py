class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # solution 1
        # cur = [0,1,0]
        # for i in range(rowIndex):
        #     cur = [0]+[cur[i]+cur[i+1] for i in range(len(cur)-1)]+[0]
        # return cur[1:-1]

        # solution 2
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row