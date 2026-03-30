class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # if there are still index and the stack and the current tempurature is warmer than the tempurature we have stored in the stack
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                # the number of days in the future when the temp wil be warmer
                ans[i] = stack[-1] - i
            stack.append(i)
        
        return ans