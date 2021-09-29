def numSum(cnt, num):
    ans = 0
    for i in range(cnt):
        ans += int(num[i])
    return ans


if __name__ == "__main__":
    cnt = int(input())
    num = input()
    print(numSum(cnt, num))

    # sum(map(int, input()))
