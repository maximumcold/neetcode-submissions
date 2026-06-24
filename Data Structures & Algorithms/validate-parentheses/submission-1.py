class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        for c in s:
            if c in "([{":
                stack.append(c)
            if c in ")]}":
                if len(stack) < 1:
                    return False
                value = stack.pop()
                if c == ")":
                    if value != "(":
                        return False
                if c == "]":
                    if value != "[":
                        return False
                if c == "}":
                    if value != "{":
                        return False

        if len(stack) <= 0: 
            return True  
        return False