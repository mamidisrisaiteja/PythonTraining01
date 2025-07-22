'''file =open("demo.txt")  #open the file
print(file.read())      #Read the file

    
file.close()            #Close the file
print("File closed successfully.") 

# Read 1st 5 characherts in the file
file = open("demo.txt") 
print(file.read(5))
file.close()
print("File closed successfully")


#Read 1st line in the file
file = open("demo.txt")
print(file.readline())
file.close()
print("File closed successfully")

# Read all lines in the file
file = open("demo.txt")     
line =file.readline()
while(line!=""):
    print(line)
    line = file.readline()
file.close()
print("File closed successfully")
'''

#Print First 2 lines of a file
file = open("demo.txt")
line1=file.readlines()
#line2=file.readline()
print(line1)
#print(line2.strip())
file.close()

