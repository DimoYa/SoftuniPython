pages_in_book = int(input())
pages_per_hour = int(input())
days = int(input())

duration_for_the_book = pages_in_book / pages_per_hour
required_days_per_day = duration_for_the_book / days

print(int(required_days_per_day))

