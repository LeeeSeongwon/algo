def repeatChar(num, str):
    ans = [s * num for s in str]
    print("".join(ans))


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        num, str = input().split(" ")
        repeatChar(int(num), str)
