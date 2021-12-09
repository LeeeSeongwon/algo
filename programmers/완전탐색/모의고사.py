def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = [0, 0, 0]
    result = []

    for item in enumerate(answers):
        idx = item[0]
        ans = item[1]
        if num1[idx % len(num1)] == ans:
            answer[0] += 1
        if num2[idx % len(num2)] == ans:
            answer[1] += 1
        if num3[idx % len(num3)] == ans:
            answer[2] += 1

    maxx = max(answer)
    for idx, student in enumerate(answer):
        if student == maxx:
            result.append(idx + 1)
    return result
