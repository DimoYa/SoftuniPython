with open("numbers.txt") as file:
    nums = file.readlines()
    sum_of_nums = 0

    for num in nums:
        sum_of_nums += int(num)

    print(sum_of_nums)
