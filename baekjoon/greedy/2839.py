def main(n):
    ans = []
    max_five = n // 5
    max_three = n // 3

    for i in range(max_five + 1):
        for j in range(max_three + 1):
            if i * 5 + j * 3 == n:
                ans.append(i + j)

    # print(ans)
    if not ans:
        return -1
    else:
        return sorted(ans)[0]


if __name__ == "__main__":
    n = int(input())
    print(main(n))
