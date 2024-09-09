deposit_sum = float(input())
duration = int(input())
interest_rate = float(input())

rate = deposit_sum * (interest_rate / 100)
monthly_rate = rate / 12
total_sum = deposit_sum + (duration * monthly_rate)

print(total_sum)

