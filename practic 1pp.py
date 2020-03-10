# Open a file to read and write
# write file
file1 = open("my file.txt", "w")
file1.write("Hello \n")
file1.writelines("This is Mumbai \n Thise is Pune \n This is Dheli \n")
file1.close()

# read file
file1 = open("my file.txt", "r+")
print(file1.read())




