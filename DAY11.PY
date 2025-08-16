
#simple exercise using ifelse and elif statements 


time = float(input("enter the time"))
if (time < 9.00):
    print("you have more time buddy go and sleep")
elif (time>9.00):
    if(time > 9.00 and time < 12.30):
        print("good morning buddy have a nice day:")
    elif(time > 12.30 and time <6.30):
        print("good afternoon budy dont forget to eat lunch")
    elif(time > 6.30):
        print("good evening buddyyyy have chai")

#time

import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if '00:00:00' <= timestamp < '12:30:00':
    print("good morning buddyyyy have a nice day")
elif '12:30:00' <= timestamp < '18:30:00':
    print("good after noon buddyyyyy it is afternoon go and take a nap")
elif '18:30:00' <= timestamp < '23:50:59':
    print("good night bussyyyy it is already late")


"""while doing this i have not got a single error but instead 
my program was giving wrong answer or stopped taking input i have learnt so much while solving 
those and also got a logical thinking too..."""