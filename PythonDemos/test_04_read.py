# To open a file and read all its contents
file = open("../demo.txt")
# To print the contents of the file
print(file.read())
# To close the file after reading
file.close()

# To open a file and read its first n characters
file = open("../demo.txt")
#To print the contents of the file until a specific number of characters
print(file.read(5))
# To close the file after reading
file.close()

# To open a file and read its 1st line
file = open("../demo.txt")
# # To print the contents of the file
print(file.readline())
# To close the file after reading
file.close()

# To open a file and read its 1st line
file = open("../demo.txt")
# To read the contents of the file until a specific number of characters
line=file.readline()
while(line!=""):
    print(line, end="")
    line = file.readline()
# To close the file after reading
file.close()

file=open("../demo.txt")
print()
print("Printing the first two lines of the file:")
count=0
line = file.readline()
while count<2:
    line = file.readline()
    print(line, end="")
    count += 1

file.close()
#Read the content using the readlines() method
print()
print("Printing the  content using the readlines() method")
file=open("../demo.txt")
for line in file.readlines():
    print(line, end="")
file.close()

