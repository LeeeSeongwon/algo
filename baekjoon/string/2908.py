if __name__ == "__main__":
    nums = input().split(" ")
    num1 = int(nums[0][::-1])
    num2 = int(nums[1][::-1])
    print(max(num1, num2))
