def solution(A):
    west_sum = 0
    len_A = len(A)
    cnt_one = sum(A)
 
    for i in range(len_A):
        if A[i] == 0:
            west_sum += cnt_one
            if west_sum > 1000000000:
                return -1
        else:
            cnt_one -= 1
 
    return west_sum