start_year = 1950
end_year = 2000

MONTH_DAYS=[31,29,31,30,31,30,31,31,30,31,30,31]
FEBRURARY = 1


for month in range(len(MONTH_DAYS)):
    max_day = MONTH_DAYS[month]
    for day in range(max_day):
        pesel_day = "%02d%02d"%(month+1, day+1)
        print("012,ACD,?d?d"+pesel_day+"?1"+4*"?d"+"?2?u?u")

