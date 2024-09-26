def sum_nums(*arg):
    negative = 0
    positive = 0

    for num in arg:
        if num < 0:
            negative += num
        elif num > 0:
            positive += num

    return negative, positive


numbers = map(int, input().split())
negative_sum, positive_sum = sum_nums(*numbers)
print(f"{negative_sum}\n{positive_sum}")

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

