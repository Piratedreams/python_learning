temps = [221, 234, 340, -999, 230]

new_temps = [temp/ 10 for temp in temps if temp != -999]


print(new_temps)