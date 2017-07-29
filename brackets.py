class BracketMatcher:
    __right_to_left = {')': '(', ']': '[', '}': '{'}

    @staticmethod
    def are_brackets_correct(l: str) -> bool:
        stack = []
        for i in l:
            if i in ('(', '[', '{'):
                stack.append(i)
            elif i in (')', ']', '}'):
                if len(stack) == 0 or BracketMatcher.__right_to_left[i] != stack.pop():
                    return False
        return len(stack) == 0
