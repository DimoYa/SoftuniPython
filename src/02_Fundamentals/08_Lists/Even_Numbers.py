nums = [int(num) for num in input().split(", ")]
even_num = [i for i in range(len(nums)) if nums[i] % 2 == 0]
print(even_num)
