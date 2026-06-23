class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
                continue
            if (char == ")"):
                if "(" not in stack:
                    return False
                elif (stack.pop() == "("):
                    continue
                else:
                    return False
            if (char == "]"):
                if "[" not in stack:
                    return False
                elif (stack.pop() == "["):
                    continue
                else:
                    return False
            if (char == "}"):
                if "{" not in stack:
                    return False
                elif (stack.pop() == "{"):
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False