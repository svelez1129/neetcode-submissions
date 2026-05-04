class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c=='[':
                stack.append(c)
            else:
                if not stack:
                    return False
                recent = stack.pop()
                if c == ')':
                    if '(' != recent:
                        return False
                elif c == '}':
                    if '{' != recent:
                        return False
                elif c == ']':
                    if '[' != recent:
                        return False
        return True if not stack else False