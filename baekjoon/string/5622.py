if __name__ == "__main__":
    # abc def ghi jkl mno pqrs tuv wxyz
    # 012 345 678 901 234 5678 901 2345
    # 2   3   4   5   6   7    8   9     0

    nums = {
        "ABC": "2",
        "DEF": "3",
        "GHI": "4",
        "JKL": "5",
        "MNO": "6",
        "PQRS": "7",
        "TUV": "8",
        "WXYZ": "9",
    }

    res = ""
    ans = 0
    input_str = input()
    for n in input_str:
        for key, value in nums.items():
            if n in key:
                res += value
                break
        else:
            res += "0"

    for num in res:
        ans += int(num) + 1

    print(ans)
