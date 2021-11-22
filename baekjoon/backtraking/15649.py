import sys
from itertools import permutations


def main(n):
    # 3 1
    _range = int(n[0])
    cnt = int(n[1])
    for i in permutations(range(1, _range + 1), cnt):
        tmp = ""
        for j in i:
            tmp += str(j) + " "
        print(tmp)


if __name__ == "__main__":
    n = input().strip().split(" ")
    main(n)
