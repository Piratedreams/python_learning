temps = [221, 234, 340, -999, 230]



# if for loop needs to be in a list, it goes at the end.
new_temps = [temp / 10 if temp != -999 else 0 for temp in temps]


print(new_temps)


