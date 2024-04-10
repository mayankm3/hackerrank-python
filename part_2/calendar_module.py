# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar

a, b, c = map(int, input().split()) #Input Format: A single line of input containing the space separated month, day and year, respectively,
day = calendar.weekday(c, a, b)
all_days_of_week = calendar.weekheader(10)
my_list = all_days_of_week.split()
print(my_list[day].upper())






#hackerrank-python witchcraft
# import calendar
# n1,n2,n3=map(int,input().split())
# print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())
#
# calendar.day_name
# An array that represents the days of the week in the current locale.