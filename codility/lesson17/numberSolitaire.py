def solution(A):
    N = len(A)
    answer = [A[0]] * (N + 6)

    for i in range(1, N):
        answer[i + 6] = max(answer[i : i + 6]) + A[i]

    return answer[-1]


if __name__ == "__main__":
    print(solution([1, -2, 0, 9, -1, -2]))
