class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                ret = stack.pop()+stack.pop()
                stack.append(ret)
            elif t == "*":
                ret = stack.pop()*stack.pop()
                stack.append(ret)
            elif t == "-":
                first = stack.pop()
                second = stack.pop()
                ret = second-first
                stack.append(ret)
            elif t == "/":
                first = stack.pop()
                second = stack.pop()
                ret = int(second/first)
                stack.append(ret)
            else:
                stack.append(int(t))
        return stack[-1]
