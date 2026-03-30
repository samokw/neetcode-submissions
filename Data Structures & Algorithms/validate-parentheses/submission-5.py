class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        # Created a map to allow us to know what closing brackets map to opening ones\
        # O(1) space complexity, O(1) retrivals
        closeToOpen = { ")": "(", "}": "{", "]":"["} 
        
        # Looping through every character in the string
        for char in s:
            # We want to check the character is a key in the map
            if char in closeToOpen:
                # If the stack is non-empty and the element at the top of the stack is matches as the value at the key
                if stack and stack[-1] == closeToOpen[char]:
                    # Remove that element from the stakc
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        # for c in s:
        #     if c in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return True if not stack else False