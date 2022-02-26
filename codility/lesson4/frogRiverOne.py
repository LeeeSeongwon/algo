def solution(X, A):
    ## o(n)
    c = [0] * (X)
    s = 0
    for idx, i in enumerate(A):
        if c[i - 1] == 0:
            c[i - 1] = 1
            s += 1
            if s == X:
                return idx

    return -1
