start_year = 1900
end_year = 2000

MONTH_DAYS=[31,28,31,30,31,30,31,31,30,31,30,31]
FEBRURARY = 1

def is_leap(year:int)->bool:
    return (((year%4==0) and (year%100!=0)) or (year%400==0))

WEIGHTS = [1,3,7,9,1,3,7,9,1,3]

def gen_control_digit(pesel):
  control=0
  for ind in range(len(WEIGHTS)):
      control+=(ord(pesel[ind])-ord('0'))*WEIGHTS[ind]
  control %= 10
  control = (10-control)%10
  return str(control)


def gen_serial(file, pesel_day):
    for i in range(0,3000):
        out = pesel_day+"%04d"%(i)
        ctrl = gen_control_digit(out)
        file.write(out+ctrl+"\n")
        

def main(out_file):        
    for year in range(start_year,end_year):
        leap_year = is_leap(year)
        print(year)
        for month in range(len(MONTH_DAYS)):
            temp_month=month+1
            if year>=2000: temp_month+=20
            max_day = MONTH_DAYS[month]
            if month==FEBRURARY and leap_year: max_day+=1
            for day in range(max_day):
                pesel_day = "%02d%02d%02d"%(year%100, temp_month, day+1)
                gen_serial(file, pesel_day)


with open("out", "wt") as file:
    main(file)
