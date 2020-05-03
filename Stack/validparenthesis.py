class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        for c in s:
            if c in d.keys():
                stack.append(c)
            else:
                try:
                    if d[stack.pop()] == c:
                        pass
                    else:
                        return False
                except:
                    return False
                
        return len(stack) == 0