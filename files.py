#file=open("myfile.txt","r") # open file and read text

#print(file.read())

# how to inser text to the file / Write operation 
# r - read, 
# a - append
# w - write (overriding) similar to erase 
file=open("myfile.txt","w")
file.write("\n3. this is third") # writing file
file.close()

file=open("myfile.txt","r")
print(file.read())