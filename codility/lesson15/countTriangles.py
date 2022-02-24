# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    cnt = len(A)
    ans = 0
    if cnt < 3:
        return 0

    A.sort()

    for i in range(cnt - 2):
        k = i + 2
        for j in range(i + 1, cnt):
            while k < cnt and A[i] + A[j] > A[k]:
                k += 1
            if k > j:
                ans += k - j - 1

    return ans
