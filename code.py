from decimal import Decimal
print 'Enter the date of your inquiry in the following format mm/dd/year. When finished hit "ENTER".'
date = raw_input()
print 'Enter the total amount of hours worked for the day from your time card. When finished hit "ENTER".'
user_imput_day = raw_input()
print 'Enter tasks in minutes separated by comas. When finished hit "ENTER".'
user_input = raw_input()
a = user_input.split(',')
b = [int(x) for x in a]
u = sum(b)#total amount of tasks completed im minuted
y = divmod(u,60)#total amount of tasks completed in hours and minutes
print 'You have completed ' + str(y[0]) + ' hours and ' + str(y[1]) + ' minutes of work on ' + date + '.'
h = u/float(60)/float(Decimal(user_imput_day))*100
print h
print 'Your productivity for ' + date + ' is ' + str(round(h,1)) + '%.'
if h < 75:
    print 'Sorry, your performance is below the required minimum. Limit your bathroom breaks OR YOU WILL GET FIRED!'
if h >= 75 and h < 80:
    print 'Your performance is on target. Keep it up!'
if h >=80:
    print 'Congratualtions - you are a pacesetter!'
