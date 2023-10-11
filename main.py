from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    }

    today = datetime.now().date()
    current_weekday = today.weekday()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        
        if 0 <= delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
            if day_of_week == "Saturday" and current_weekday != 0:
                birthdays_per_week["Monday"].append(name)
            elif day_of_week == "Sunday" and current_weekday != 0:
                next_monday = today + timedelta(days=(7 - current_weekday) + 2)
                birthdays_per_week["Monday"].append(name)
            else:
                birthdays_per_week[day_of_week].append(name)

    
    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Olivia Brown", "birthday": datetime(1998, 1, 10)},
    {"name": "Alexander Wilson", "birthday": datetime(2001, 11, 2)},
    {"name": "Lucas Baker", "birthday": datetime(1997, 10, 20)},
    {"name": "Sophie Anderson", "birthday": datetime(1996, 10, 10)},
    {"name": "Ella Wilson", "birthday": datetime(1999, 10, 11)},
    {"name": "Benjamin Clark", "birthday": datetime(2002, 10, 12)},
    {"name": "Oliver Smith", "birthday": datetime(1989, 10, 13)},
    {"name": "Isabella Martin", "birthday": datetime(2004, 10, 14)},
    {"name": "Mia Davis", "birthday": datetime(1994, 10, 15)},
]

get_birthdays_per_week(users)
        
