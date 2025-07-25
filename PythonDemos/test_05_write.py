#This is used as alternative to file =open('demo.txt) file.close() r-read w-write
with open('../demo.txt', 'r') as reader:
    content=reader.readline()
    reversed(content)   #in python we have a function to reverse the content
    with open('../demo.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)