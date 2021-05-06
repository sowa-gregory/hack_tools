start_year = 1900
end_year = 2000

MONTH_DAYS=[31,28,31,30,31,30,31,31,30,31,30,31]
FEBRURARY = 1

def is_leap(year:int)->bool:
    return (((year%4==0) and (year%100!=0)) or (year%400==0))

for year in range(start_year,end_year+1):
    leap_year = is_leap(year)
    for month in range(len(MONTH_DAYS)):
        temp_month=month+1
        if year>=2000: temp_month+=20
        max_day = MONTH_DAYS[month]
        if month==FEBRURARY and leap_year: max_day+=1
        for day in range(max_day):
            pesel_day = "%02d%02d%02d"%(year%100, temp_month, day+1)
            print(pesel_day+"?d"*5)
 
