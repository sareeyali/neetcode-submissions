class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i, c in enumerate(tokens):
            if c.lstrip('-').isdigit():

                stack.append(c)
                continue
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            exp = str(num2) + c + str(num1)
            res = eval(exp)
            stack.append(res)

        return int(stack[-1])
