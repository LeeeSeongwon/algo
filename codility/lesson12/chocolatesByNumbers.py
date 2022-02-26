# Euclidean algorithm


# def solution(N, M):
#     choco = [1 for _ in range(N)]

#     ans = 0
#     i = 0
#     while choco[i] != 0:
#         if i == 0:
#             choco[i] = 0

#         choco[i] = 0
#         ans += 1
#         i = (i + M) % N

#     return ans


def solution(N, M):
    return N // getGCD(N, M)


def getGCD(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return getGCD(b, a % b)


if __name__ == "__main__":
    print(solution(10, 4))
