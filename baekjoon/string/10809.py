def findAlphabet(input):
    alpha = list(range(97, 123))
    for a in alpha:
        print(input.find(chr(a)))


if __name__ == "__main__":
    findAlphabet(input())
