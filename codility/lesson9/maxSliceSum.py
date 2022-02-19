def solution(A):
    ## 카데인 알고리즘
    if len(A) == 1:
        return A[0]

    localMaxSum = A[0]
    globalMaxSum = A[0]

    for i in range(1, len(A)):
        localMaxSum = max(A[i], localMaxSum + A[i])
        globalMaxSum = max(globalMaxSum, localMaxSum)

    return globalMaxSum
