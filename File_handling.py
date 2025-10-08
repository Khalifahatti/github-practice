# file1 = open(r"C:\Users\Khalifah\Desktop\Text 1.txt","r")
# print(file1.read(10))
# file1.close()

# file_write = open("test.txt", "w")
# file_write.write("This is for write mode")
# file_write.close()

# file_a = open("test.txt", "a")
# file_a.write("\nThis is a newly appended line")
# file_a.close()

# file_c = open("new.txt", "x")
# file_c.write("This is a newly created file")
# file_c.close


with open("new txt", "r") as file1:
    content = file1.read()
    print(content)
