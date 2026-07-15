class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if ops == "+":
                b = stack.pop()
                a = stack.pop()
                total = a + b
                stack.append(a)
                stack.append(b)
                stack.append(total)
            elif ops == "C":
                stack.pop()
            elif ops == "D":
                last = stack.pop()
                double = 2 * last
                stack.append(last)
                stack.append(double)
            else:
                stack.append(int(ops))
        return sum(stack)