class Solution:
    def climbStairs(self, n: int) -> int:
        
    

        def climb(i):

            # If the level we are is greater than or equal to the top level return i
            if i >= n:
                return i == n
            return climb(i + 1) + climb(i + 2)
        
        
        
        return climb(0)

