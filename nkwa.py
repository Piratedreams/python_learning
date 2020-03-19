myfile =  open("fruits.txt")

content = myfile.read()
myfile.close()


# opening files using with
with open('files/vegetables.txt') as myfile:
    myfile.wrtie('tomato')

print(content)


