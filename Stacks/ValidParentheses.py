# Literally how you learn about stacks ahh question
def isValid(self, s: str) -> bool:
        dic = {}
        dic[')'] = '('
        dic['}'] = '{'
        dic[']'] = '['
        stack = []
        for x in s:
            if x in dic:
                if stack and dic[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return len(stack) == 0
