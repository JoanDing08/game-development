#make a file with numbers
#display their sum on the screen

with open("number file","w") as file:
    file.write("1,2,3,4,5,6,7,8,9,10")
with open("number file") as file:
    print(file.read())

with open("sum","w") as file:
    file.write("55")
with open("sum") as file:
    print("the sum of these numbers is",file.read())
