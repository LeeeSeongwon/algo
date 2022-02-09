from itertools import combinations

def main(cnt, target, listA):
    ans = 0

    for i in range(1, cnt+1):
        comb = combinations(listA, i)
        for sub in comb:
            if sum(sub) == target:
                ans +=1
    return ans

if __name__ == "__main__":
    cnt, target = map(int, input().split(" "))
    listA = list(map(int, input().split(" ")))

    print(main(cnt, target, listA))
