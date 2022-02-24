# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    cnt = len(A)
    if cnt == 1:
        return 0 if A[0] < K else 1

    ans = 0
    temp = 0
    for i in range(cnt):
        if A[i] >= K:
            ans += 1
            temp = 0
        else:
            if temp and temp + A[i] >= K:
                ans += 1
                temp = 0
            elif temp:
                temp += A[i]
            else:
                temp = A[i]

    return ans
