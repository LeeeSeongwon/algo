def main(target, coin_types):
    cnt = 0
    for i in reversed(range(len(coin_types))):
        cnt += target // coin_types[i]
        target = target % coin_types[i]
    return cnt


if __name__ == "__main__":
    coin_cnt, target = map(int, input().split())
    coin_types = list()
    for i in range(coin_cnt):
        coin_types.append(int(input()))

    print(main(target, coin_types))
