class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []

        def dfs(op, cl):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if op < n:
                path.append("(")
                dfs(op + 1, cl)
                path.pop()
            if cl < op:
                path.append(")")
                dfs(op, cl + 1)
                path.pop()
        dfs(0, 0)
        return res