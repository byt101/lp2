a = input(str("Enter a string: "))
b = 127
c = b and a
d = [chr(ord(x)^ord(y)) for x,y in zip(a,str(b))]
print(c)
print(d)