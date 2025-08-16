#as the part of day 10 learning python today i am going to ;earn about if else statement in python 

# conditional operators 
# <, >, <= , >= , == , !=.

a= int(input("enter ur naumber: "))
print("entered number is")
print(a<18)
print(a>18)
print(a<=18)
print(a>=18)
print(a==18)
print(a!=18)


# if

a= int(input("enter you age"))
print("your age is: ", a)
if (a>18):
    print("you are eligible to drive")
else:
    print("you are not eligible for it")


appleprice = int(input())
print("appleprice is: ", appleprice)
budget = 500 
if (appleprice <= budget):
    print("sunnyy add 1 kg of apples to the kart")
else:
    print("budget is less than the price of apples")


# elif

num = int(input("enter you number :"))
print("entered value is :" , num)
if (num < 0):
    print("num is negative")
elif (num == 0):
    print("num is equal to 0")
else:
    print("num is positive")

print("woww i am happyy thank u python!")

# nested if

num = int(input("enter ur number :"))
if (num < 0):
    print("number is negative: ")
elif (num > 0):
    if (num <= 10):
        print("number is between 1-10 :")
    elif(num> 10 and num <=20):
        print("number is between 10-20: ")
    else:
        print("number is greater than 20")
else:
    print("number is zero")