def main(target):
    change = [500, 100, 50, 10, 5, 1]
    ans = 0
    # 최소 개수의 거스름돈
    for i in range(len(change)):
        ans += target // change[i]
        target = target % change[i]
    return ans


if __name__ == "__main__":
    target = int(input())
    print(main(1000 - target))
