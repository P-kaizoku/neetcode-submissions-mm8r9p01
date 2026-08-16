class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = set(["+", "*", "/", "-"])

        def calc(a, b, op):
            match op:
                case "+":
                    return a+b
                case "-":
                    return a-b
                case "/":
                    return int(a/b)
                case "*":
                    return a*b

        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(calc(a, b, t))
                continue


            stack.append(int(t))

        return stack[-1]
