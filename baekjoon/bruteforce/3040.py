from itertools import combinations


def findSevenDwarf(dwarf):
    for candidate in combinations(dwarf, 7):
        if sum(candidate) == 100:
            return candidate


if __name__ == "__main__":
    dwarf = list()
    for _ in range(9):
        dwarf.append(int(input()))

    ans = findSevenDwarf(dwarf)
    for i in ans:
        print(i)
