def Feb(year): # 先判定是平年还是闰年,再给出每个月的天数
    Feb_day = 29
    if year%100 !=0:  # 非整百年
        if year%4 == 0:
            Feb_day = 28
    elif year%100 == 0:  # 整百年
        if year%400 == 0:
            Feb_day = 28
    elif year >= 3200:   # 数值很大的年份
        if year%3200 == 0 and year%172800 == 0:
            Feb_day = 28
    return Feb_day        
    
input_day = list(map(int,input().split('/')))
Feb_day = Feb(input_day[0])
Feb_day = str(Feb_day)
months = str('31,0,31,30,31,30,31,31,30,31,30,31')
months = months.replace('0',Feb_day,1) # 12个月每个月有多少天

month = input_day[1] # 第2个位置上是月份
day = input_day[2] # 第3个位置上是日期

if month == 1:
    count_day = day
elif month != 1:
    count_day = sum(eval(months)[0:month-1])+day
    
print(count_day)