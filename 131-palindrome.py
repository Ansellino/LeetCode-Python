class Solution:
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def isPal(self, s):
        return s == s[::-1]
    
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
    
'''
class Solution:
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def isPal(self, s):
        return s == s[::-1]

    def dfs(self, s, path, res):
        if not s:
            res.append(path[:])  # Append a copy of the path to avoid modifying it
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                path.append(s[:i])
                self.dfs(s[i:], path, res)
                path.pop()  # Backtrack by removing the last added prefix
'''