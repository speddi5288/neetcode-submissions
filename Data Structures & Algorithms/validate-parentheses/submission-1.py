class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing -> opening
        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            # If it's a closing bracket, it must match stack top
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Otherwise it's an opening bracket
                stack.append(c)

        # Valid only if all opens were matched
        return len(stack) == 0
