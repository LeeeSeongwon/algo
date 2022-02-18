# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    sum_one_more = sum([i for i in range(1, len(A)+2)])
    sum_A = sum(A)

    return sum_one_more - sum_A

