class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "-", "/", "*"}
        if not tokens:
            return 0
        
        stack = []
        for tkn in tokens:
            if tkn == "+":
                stack.append(stack.pop()+stack.pop())
            elif tkn == "-":
                stack.append(-(stack.pop()-stack.pop()))
            elif tkn == "*":
                stack.append(stack.pop()*stack.pop())
            elif tkn == "/":
                
                stack.append(int(stack.pop(-2)/stack.pop()))
            else:
                stack.append(int(tkn))
        return stack.pop()