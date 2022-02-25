def solution(A, B):

    ## 조건 확인 잘하자
    if not B:
        return 0

    ans = 1
    end = B[0]
    for i, item in enumerate(A):
        if i == 0:
            continue
        else:
            if item > end:
                ans += 1
                end = B[i]

    return ans
            
if __name__ == "__main__":
    solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10])