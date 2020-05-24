# try/except

str1 = "Hello, world"
try:
    istr = int(str1)
    print("statement1")
except:
    istr = -1
print(istr)

str2 = "123"
try:
    istr = int(str2)
    print("statement2")
except:
    istr = -1
print(istr)
