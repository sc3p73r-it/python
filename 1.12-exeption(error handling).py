try:
    files= open("msg.txt","r")

except IOError:
    print("File not Found")

else:
    print(files.read())