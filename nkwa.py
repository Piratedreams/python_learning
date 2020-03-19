myfile =  open("fruits.txt")

content = myfile.read()
myfile.close()


# opening files using with
with open('fruits.txt') as myfile:
    content = myfile.read()

print(content)


