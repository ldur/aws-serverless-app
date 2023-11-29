from datetime import datetime, timedelta

def days_until_christmas():
    
    today = datetime.now().date()
    christmas = datetime(today.year, 12, 24).date()

    if today > christmas:
       christmas = datetime(today.year + 1, 12, 24).date()

    delta = christmas - today
    days = str(delta.days) + " days until Christmas!"
    return days

print(days_until_christmas())
