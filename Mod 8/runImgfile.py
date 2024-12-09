filename = "F:\pics\IMG_20210425_160027.jpg"
file2 = "faisal_copy.png"

# as Image file are binary files, So we need to use rb as mode
with open(filename, mode="rb") as tay:
    content = tay.read()
   #print(type(content))

with open(file2, mode= "wb") as fp:
    content = fp.write(content)
    print(content)
print("Done copying Image!")