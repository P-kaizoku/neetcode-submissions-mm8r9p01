class Solution:
    def operate(self, a: str, b: str, o: str):
        
        match o:
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
        operators = {"+", "-", "/", "*"}

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                res = self.operate(a,b,i)
                stack.append(res)
        
        return stack[0]