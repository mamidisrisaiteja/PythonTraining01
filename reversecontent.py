file = open("demo.txt")
content=file.read()

reversed_content=content[::-1]
print(reversed_content)
file.close()

