# today i am going to learn about typecasting in python
a="7"
b="10"
print(int(a)+int(b))



a="17.88" 
b="77" 
print(float(a)+int(b))

#exiplicit typecasting 


sunny = "99"
thrishanth = "99"
thrishanth_sunny = int(sunny)
sum = int(sunny) + int(thrishanth)
print("the sum of sunny and thrishanth is", sum)


#implicit typecasting


a = 100
print(type(a))
b = 99.9
print(type(b))

c = a+b
print(c)
print(type(c))

