#Реализуйте функцию принимающую 2 аргумента - 2-е даты. Результатом вычисления функции должна быть разница 
#между 2-й датой и 1-й датов в днях. В случае если разница принимает негативное значение вывести в консоль 
#абсолютное значение разницы в днях. Используем стандартный модуль Python для работы с датами datetime 
#(без внешних библиотек).
import datetime
from datetime import datetime, timedelta
def count_day_subs(d1, d2):
    
    s1 = datetime.strptime(d1,"%d.%m.%Y")
    s2 = datetime.strptime(d2,"%d.%m.%Y")
    
    s3 = s1 - s2
    
    if s3.days >= 0:
        return s3.days
    else:
        return abs(s3.days)

def count_day(d1):
    d1_splited = d1.split(".")
    d1_days = int(d1_splited[0]) 
    d1_month = int(d1_splited[1])
    d1_year = int(d1_splited[2])

    d1_days += d1_month *31
    if d1_month >= 2:
        if d1_year % 100 != 0:
            if(d1_year % 4 != 0): 
                d1_days -= 3
            else:
                d1_days -= 2
        elif d1_year % 400 !=0:
            d1_days -= 3
        else:
            d1_days -=2
    
    if d1_month >= 4 and d1_month < 6:
        d1_days -= 1
    elif d1_month >= 6 and d1_month < 9:
        d1_days -= 2
    elif d1_month >=9 and d1_month < 11:
        d1_days -= 3
    elif d1_month >= 11:
        d1_days -= 4
    
    d1_days += d1_year * 365 + ((d1_year // 4) - (d1_year // 100) + (d1_year // 400))

    return d1_days

def call_count_day(data1, data2):
    res = count_day(data1) - count_day(data2)
    if res >= 0:
        return res
    else:
        return abs(res) 

print(count_day_subs("22.01.1991","30.12.2022"))
print(call_count_day("22.01.1991","30.12.2022"))