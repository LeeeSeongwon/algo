def main(n, input_num):
    # 산술평균 : N개의 수들의 합을 N으로 나눈 값
    # 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    # 최빈값 : N개의 수들 중 가장 많이 나타나는 값
    # 범위 : N개의 수들 중 최댓값과 최솟값의 차이

    print(round(sum(input_num) / n))
    sorted_num = sorted(input_num)
    print(sorted_num[int(n / 2)])
    print(most_frequent(sorted_num))
    print(sorted_num[-1] - sorted_num[0])


def most_frequent(sorted_arr):
    ans = []
    max = 0
    freqent = 0
    if len(sorted_arr) == 1:
        return sorted_arr[0]

    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] == sorted_arr[i + 1]:
            freqent += 1
            if i+1 == len(sorted_arr) -1:
                
        else:
            if freqent >= max:
                max = freqent
                ans = [sorted_arr[i]]
            elif freqent == max:
                ans.append(sorted_arr[i])
            else:
                continue

    print(ans)
    if len(ans) == 1:
        return ans[0]
    else:
        return sorted(ans)[1]


if __name__ == "__main__":
    n = int(input())
    input_num = []
    for i in range(n):
        input_num.append(int(input()))

    main(n, input_num)
