basketball_shoes = 0.4
basketball_clothes = 0.2
basketball = 0.25
basketball_accessories = 0.2

annual_amount = float(input())

price_basketball_shoes = annual_amount * (1 - basketball_shoes)
price_basketball_clothes = price_basketball_shoes * (1 - basketball_clothes)
price_basketball = price_basketball_clothes * basketball
price_basketball_accessories = price_basketball * basketball_accessories

total_amount = annual_amount + price_basketball_shoes + price_basketball_clothes + price_basketball + price_basketball_accessories
print(total_amount)
