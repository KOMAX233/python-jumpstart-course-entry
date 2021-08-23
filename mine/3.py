import datetime
def birth():
    print("-----------------------------------")
    print("         BIRTHDAY APP")
    print("-----------------------------------\n")
    year = input("What year were you born [YYYY]? ")
    month = input("What month were you born [MM]? ")
    day = input("What day were you born [DD]? ")
    today = datetime.date.today()
    print("It looks like you were born on " + day + "/" + month + "/" + year)
    if (month == str(today.month) and day == str(today.day)):
        birthday = datetime.date(int(year), int(month), int(day))
        nextbirthday = datetime.date(today.year, int(month), int(day))
        age = birthday - today
        delta = nextbirthday - today
        print("Looks like your", round(-age.days/365), "th birthday is in", delta.days, "days.")
        print("Happy Birthday!")
    elif (int(month) > today.month or (int(month) == today.month and int(day) > today.day)):
        birthday = datetime.date(int(year), int(month), int(day))
        nextbirthday = datetime.date(today.year, int(month), int(day))
        age = birthday - today
        delta = nextbirthday - today
        print("Looks like your", round(-age.days/365), "th birthday is in", delta.days, "days.")
        print("Hope you're looking forward to it!")
    else:
        birthday = datetime.date(int(year), int(month), int(day))
        nextbirthday = datetime.date(today.year+1, int(month), int(day))
        age = birthday - today
        delta = nextbirthday - today
        print("Looks like your", round(-age.days/365)+1, "th birthday is in", delta.days, "days.")
        print("Hope you're looking forward to it!")

birth()
