nylon = float(input())
paint = float(input())
thinner = int(input())
hours = int(input())

additional_nylon = 2
additional_paint_in_per = 0.1

price_of_protective_nylon = 1.50
price_of_paint = 14.50
price_of_thinner = 5.00
price_of_bags = 0.4

total_nylon = (nylon + additional_nylon) * price_of_protective_nylon
total_paint = (paint + (paint * additional_paint_in_per)) * price_of_paint
total_thinner = thinner * price_of_thinner
total_materials = total_nylon + total_paint + total_thinner + price_of_bags
total_workers = (total_materials*0.30) * hours

final_amount = total_materials + total_workers
print(final_amount)



