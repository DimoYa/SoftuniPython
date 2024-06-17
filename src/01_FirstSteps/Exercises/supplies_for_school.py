pencils = int(input())
markers = int(input())
cleaner = float(input())
discount = float(input())

pencil_price = 5.80
marker_price = 7.20
cleaner_price = 1.20

total_pencil = pencils * pencil_price
total_marker = markers * marker_price
total_cleaner = cleaner * cleaner_price

total_price = total_pencil + total_marker + total_cleaner

discount_total_price = total_price * (1-0.25)

print(discount_total_price)
