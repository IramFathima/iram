#to open file write
p=open("2.txt","w")
p.write("hello frnds")

# to read the file
p=open("2.txt","r")
p.read()
#the file will be written only in txt fil
# And you will get the output 

#to appent the txt 
p=open("2.txt","a")
p.write(" how r u ")
# to read that file write the mode again
p=open("2.txt","r")
p.read()
# you will get the output. 

# to close the file
p.close() 
