"""
files = open("msg.txt", 'a')
files.write("Hello World, this is new cointent.")
files.close()
files = open("msg.txt", "r")
print (files.read())
"""

files = open("msg.txt", 'w')
files.write("Hello World")
files.close()
files = open("msg.txt",'r')
print(files.read())