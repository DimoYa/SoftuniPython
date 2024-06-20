peters_budget = float(input())
num_video_cards = int(input())
num_processors = int(input())
num_ram_modules = int(input())

video_card_price = 250.00

video_card_amount = num_video_cards * video_card_price
processors_amount = num_processors * (video_card_amount * 0.35)
ram_modules_amount = num_ram_modules * (video_card_amount * 0.1)

total_amount = video_card_amount + processors_amount + ram_modules_amount

if num_video_cards > num_processors:
    total_amount *= (1-0.15)

diff = abs(peters_budget - total_amount)

if peters_budget >= total_amount:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
    