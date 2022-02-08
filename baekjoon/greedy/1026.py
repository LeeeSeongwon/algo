def main(listA, listB):
    ans = 0
    for i, j in zip(listA, listB):
        ans += i*j
    return ans


if __name__ == "__main__":
    cnt = int(input())

    listA = map(int, input().split(" "))
    listB = map(int, input().split(" "))

    print(main(sorted(listA), sorted(listB, reverse=True)))
