class Solution:
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(open_count, close_count, path):
            # If the current string is of length 2*n, add to results
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            
            # Add '(' if we still can
            if open_count < n:
                path.append('(')
                backtrack(open_count + 1, close_count, path)
                path.pop()
            
            # Add ')' if it won't lead to invalid sequence
            if close_count < open_count:
                path.append(')')
                backtrack(open_count, close_count + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
