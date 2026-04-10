class Solution:
    def evaluate(self, a, b, opr):

        match opr:
            case "+":
                return a+b
            case "-":
                return a-b
            case "*":
                return a*b
            case "/":
                return int(a/b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c.lstrip("-").isdigit():
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                res = self.evaluate(a, b, c)
                stack.append(res)

        return stack[0]