# file handling
# file1=open("C:\\Users\\jobin jose\\OneDrive\\Desktop\\sample.txt",'r')
# print(file1.read())
# file2=open("C:\\Users\\jobin jose\\OneDrive\\Desktop\\sample2.txt",'w')
# file2.close()


# file3=open("C:\\Users\\jobin jose\\OneDrive\\Desktop\\sample.txt",'w')
# file3.write("This is new command")
# file3.close()

# file1=open("C:\\Users\\jobin jose\\OneDrive\\Desktop\\sample.txt",'r')
# print(file1.read())

# file2.write
# file3=open("NEW TEXT.txt",'r')
# print(file3.read())

# file3=open("NEW TEXT.txt",'a')
# file3.write("\nThis is a new line")
# file3.close()
file3=open("NEW TEXT.txt",'r')
# print(file3.read())
print(file3.readline(10))
# print(len(file3.readlines()))



with open("sample.tct",'r') as file1:
    data = file1.read()
    print(data)
    # print(fil
    # e1.read())
#     print(data.split())
#     print(len(data.split())) #to find the word count in a text file