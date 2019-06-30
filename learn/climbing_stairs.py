"""
爬楼梯问题本质上是斐波那契数列，当有N阶台阶时，到达第N阶是N-1阶和N-2阶两种情况的和
"""
class Solution(object):
    def climbStairs(self, N):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def recu_fib(N):
            if N in cache:
                return cache[N]
            
            if N < 2:
                result = N
            else:
                result = recu_fib(N-1) + recu_fib(N-2)
            cache[N]=result
            return result
        return recu_fib(N)