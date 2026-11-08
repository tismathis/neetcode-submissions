class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        operators = {"+", "-", "*", "/"}

        while i < len(tokens):
            t = tokens[i]

            if t not in operators:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                else:  # "/"
                    res = int(a / b)
                stack.append(res)

            i += 1

        return stack[0]