#matchcase statements 

"""match case statement is for to comapare the
 main variable with give different patterns"""

x = 4 

match x:
    
    case 0 :
        print("x is xero")

    case 4 :
        print("case is 4")
    case _:
        print("x is < 10")


vote = str(input("do you want to vote"))

match vote:

    case _ if vote == "no":
        print("thank u, you are not voting")\
        
    case _ if vote == "yes":
        print("you can cast your vote")