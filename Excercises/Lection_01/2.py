packet_pshono = 18
packet_sugar = 12
money_for_pshono = 54
quant_of_pshono = money_for_pshono // packet_pshono

print(quant_of_pshono)

quant_of_sugar = quant_of_pshono
money_for_sugar = quant_of_sugar * packet_sugar

total_sum = money_for_pshono + money_for_sugar
print(total_sum)