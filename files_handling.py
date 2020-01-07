# File objects
f = open("text.txt", "r")
# open for reading ,writing, apending or reading and writing both
# i.e r ,w ,a r+

print(f.name)
print(f.mode)
f.close()

# opening the file in CONTEXT MANAGER using with

with open("text.txt") as f:
    file_content = f.read()
    print(file_content)
    file_content1 = f.readlines()
    print(file_content1)
    for lines in f:
        print(lines, end=" ")
# You dont wanna run outta memory when opening a very large files right?
# best to always open files this way
print(f.closed)

print(abs(12 + 12j))
print(help(f))


# with open("text.txt","r+") as f:
#     for lines in f:
#         print(lines,  end=" ")


# ? READING THE WHOLE FILE CONTENT WTIHOUT ANY LEAK OR SO
with open("text.txt", "r+") as f:
    size_to_read = 100

    file_content = f.read()
    while len(file_content) > 0:
        print(file_content, end=" ")
        file_content = f.read(size_to_read)
 # SEEK AND TELL FUNCTIONS
with open("text.txt", "r+") as f:
    size_to_read = 10
    f_content = f.read(size_to_read)
    print(f_content)
    print(f.tell())
    f.seek()

    f_content = f.read(size_to_read)
    print(f_content)

# WRITING TO THE FILE

with open("text_2.txt", "w") as f:
    f.write("testing the writing function here")


# sssssssssssseeeeeeeeeeeeeeeeeeeeekkkkkkkkkkkkkk

# READ AND WRITE mode
# COPY FROM ONE FILE TO ANOTHER
with open('gede.JPG', "rb") as rf:
    with open("gedecopy.JPG", "wb") as wf:
        funk_size = 4090
        file_content = rf.read(funk_size)
        while len(file_content) > 0:
            wf.write(file_content)
            # just to avoid the infinte loooop   shoop shooop
            file_content = rf.read(funk_size)
# okayyy that's all for now

        for line in rf:
            wf.write(line)
