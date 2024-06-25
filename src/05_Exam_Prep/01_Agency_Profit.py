avio_name = input()
count_of_tickets = int(input())
count_of_kids_ticket = int(input())
ticket_price = float(input())
service_price = float(input())

net_kids_ticket = ticket_price * (1- 0.7)
net_adult_price = ticket_price + service_price
net_kids_total = net_kids_ticket + service_price

total_tickets = count_of_tickets * net_adult_price + count_of_kids_ticket * net_kids_total

profit = total_tickets * 0.2

print(f'The profit of your agency from {avio_name} tickets is {profit:.2f} lv.')
