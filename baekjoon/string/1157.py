def wordStudy(input):
    preq = {}
    for w in input:
        if w in preq:
            preq[w] += 1
        else:
            preq[w] = 1

    maxVal = max(preq.values())
    ans = [k for k, v in preq.items() if v == maxVal]
    if len(ans) > 1:
        print("?")
    else:
        print(ans[0])


if __name__ == "__main__":
    n = input().upper()
    wordStudy(n)
