class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # All open brackets will be pushed onto the stack
        mapping = {']': '[', '}': '{', ')': '(' } # using a map to keep track of which closing brackets map to what closing brackets

        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack

"""
Lets trace through an example
Input: s = "([{}])"
                 . 

stack = []


"""
        