#make a file with numbers
#display their sum on the screen

with open("number file","w") as file:
    file.write("1,2,3,4,5,6,7,8,9,10")
with open("number file") as file:
    print(file.read())


#make a file with content and make a dicitonary for each word to count the occurances
#display the top five most common words out of 10

with open("word file.txt","r") as file:
    word_file=file.read()
word_list={"the":0,"that":0,"these":0,"there":0,"those":0,"they":0,"then":0,"than":0,"this":0,"though":0}
i give up.