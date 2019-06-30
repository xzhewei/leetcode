class Solution(object):
    def fib(self, N):
        """
        :type N: int
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
