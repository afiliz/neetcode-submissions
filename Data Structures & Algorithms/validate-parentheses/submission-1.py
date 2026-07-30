class Solution:
    def isValid(self, s: str) -> bool:
        # use stack
        # add a bracket type to stack, remove when encounter end bracket

        stack = []

        for bracket in s:
            if bracket == '{' or bracket == '[' or bracket == '(':
                stack.append(bracket)
            else:
                if not stack:
                    return False
                start_bracket = stack.pop()
                if start_bracket == '{' and bracket != '}':
                    return False
                elif start_bracket == '(' and bracket != ')':
                    return False
                elif start_bracket == '[' and bracket != ']':
                    return False
        if len(stack) > 0:
            return False
        else:
            return True