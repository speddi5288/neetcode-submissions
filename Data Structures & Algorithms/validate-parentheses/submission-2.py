class Solution:
    def isValid(self, s: str) -> bool:
        
        mapp = {'(':')', '{':'}', '[':']'}
        stk = []
        
        for c in s:
            # opening parenthesis
            if c in mapp:
                stk.append(c)
            else:
                # for closing parenthesis
                if not stk or mapp[stk.pop()] != c:
                    return False
        
        return len(stk) == 0


        