def solution(S):
    stack = []
    pair = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    for i in S:
        if i in ["(", "{", "["]:
            stack.append(i)
        else:
            if not stack:
                return 0
            if stack.pop() is not pair.get(i):
                return 0
    if stack:
        return 0
    return 1