def solution(N):
    ans = 0

    for i in range(1, int(N ** (1 / 2)) + 1):
        if N % i == 0:
            ans += 1
            if (i ** 2) != N:
                ans += 1

    return ans


if __name__ == "__main__":
    solution(24)
