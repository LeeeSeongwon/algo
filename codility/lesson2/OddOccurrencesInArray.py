def solution(A):
    shown = {}
    for item in A:
        if not shown.get(item):
            shown[item] = 1
        else:
            shown.pop(item)

    return list(shown.keys())[0]


## time complexity: O(N) or O(N*log(N))