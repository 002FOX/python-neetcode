# Valid if n = opened = closed
# if opened = n only add closed
# if closed < n and opened != n can add both
def backtrack(self, result: List[str], n: int, opened: int, closed: int, string: str):
        if len(string) == 2*n:
            result.append(string)
        if opened != n:
            self.backtrack(result, n, opened + 1, closed, string + '(')
        if closed < opened:
            self.backtrack(result, n, opened, closed + 1, string + ')')
def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(result, n, 0, 0, "")
        return result
