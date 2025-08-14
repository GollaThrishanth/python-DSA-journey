#STRING METHODS IN PYTHON

a = "thrishanth"
print(a.upper())

a = "thrishanth!!!!"
print(a.upper())
print(a.rstrip("!"))
print(len(a))
print(a[0:4])


a ="thrishanth"
print(a.replace("thrishanth" , "sunnyy"))

#upper
#upper method is used to change the user given input to upper case letters 
b = "thrishanth"
print(b.upper())

#rstrip
#rsstrip is used to remove the symbols which we mention in the rstrip string "" it removes only which are written in the end of sentence 
c="thrishanth!!!!"
print(b.rstrip("!"))

#replace 
#replace is used to replace the user given input with other input it can be used in large or big sentences 
d="thrishanth"
print(d.replace("thrishanth" , "sunny"))

#split
#split method is used to split the user given input it just reads the input and then it turns input into form of a list 

e = "sunnyy thrishanth man boy real reel instagram life"
print(e.split())

#capitalize 
#capitalize is used to capitalize the first letter of a user given word 

f = "thrishanth"
print(f.capitalize())

#center 
#center is used to bring the user given input into center using numbers 

g = "welcome to my world"
print(len(g))
print(len(g.center(50)))

h = "welcome to my world boys"
print(h.center(50 , "*"))


# count
#count method is used to find the specified word in given input like finding how many times i have written python in following statement this method helps me to find it

j = """ hello i am thirshanth and i am learning python from basics without having any knowledge in coding yess i have
learnt c language but not found any use full thing with but learning python is a wrok with full of fun """
print(j.count("python"))

#endswith
#endswith is used when the user gives an input to it if that matchs with the last word of sentence then it gives true statement 

k = "welcome to my world where me and my laptop do romance all day and night with out protection to eyes hahahhh"
print(k.endswith("eyes"))

kk = "wlecome to my world"
print(kk.endswith("to" [2 : 3]))



#find
#find is used to find the specified word in the statement 
l = "thrishanth is a good boy he knows only onething and that is how to love someone"
print(l.find("is"))

#index
#if we give something that is not in find then it returns with -1 in output to ignore it index is used after the find 
z= "thrishanth is my man"
print(z.find("$"))
# print(z.index("$"))


#isalnum
#it is only used for A-Z a-z and 0-9
#isalnum is a string which consists only A-Z, a-z and 0-9 is this are present in the following code than the output returns with "true" or else if anyother symbol is used then it shows "false"


x= "welcome to my world"
print(x.isalnum()) #in output it shows false because i have used "space".


#isalpha
#isalpha is used to check if there are only A-Z and a-z letters if not it gives false
str1 = "thrishanth is a bad boy"
print(str1.isalpha())

#islower 
#islower is used to check if the statement is in lower case or not 
str2 = "thrishanth"
print(str2.islower())

#isprintable
#isprintable is used to print only the printable statements or else it return us with an "false"
str3 = "thrishanth\n"
print(str3.isprintable())  #output is false 

#isspace 
#isspace method returns true only and only if the string contains white spaces, else returns false

str4 = "          "
print(str4.isspace())

#istile 
#istitle is used to check if the given input is a title or not if the every first letter of word is in upper case then it gives true 

str5 = " What Are You Doing"
print(str5.istitle())

#isupper 
#isupper is smilar to islower

str6 = "HEY "
print(str6.isupper())

#startswith
#startswith is used to check wether it starts with user specified letter or word 
str7 = "hey i am learning python"
print(str7.startswith("i"))

#swapcase
#swapcase changes the given input into uppercase if it is in lower case or from upper case to lowercase 
str8 = "hey buddy i am doing it"
print(str8.swapcase())

#title 
#title is used to change the given statement into title 

str9 = "hey i am billa"
print(str9.title())