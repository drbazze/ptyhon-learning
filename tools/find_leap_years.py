def calculate_leap_year(year):
    if year % 4 == 0: #evenly divisible by 4
        if year % 100 == 0:
            if year % 400 == 0: #unless the year is also evenly divisible by 400
                return True
            else:
                return False
        else: #except every year that is evenly divisible by 100
            return True
    else:
        return False
    
#Run this part when the file is executed as a script
if __name__ == "__main__":
    #range of years
    years = range(1900, 2401)

    #show the leap years only
    for year in years:
        is_leap_year = calculate_leap_year(year)

        if is_leap_year:
            print (f"{year} - yes")