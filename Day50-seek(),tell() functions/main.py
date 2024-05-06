# with open('myfile.txt', 'r') as f:
#     print(type(f))

#     f.seek(10)
#     # Move to the 10 bytes in the file
    
#     print(f.tell())
#     data = f.read(5)
#     print(data)
#     # Read the next 5 bytes

with open('sample.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(4)

with open('sample.txt', 'r') as f:
    print(f.read())