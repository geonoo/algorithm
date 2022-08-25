from datetime import datetime, date

def solution(a, b):
    return what_day_is_it(date(2016, a, b))



def what_day_is_it(date):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()
    return(days[day])


print(solution(5,24))