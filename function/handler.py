from datetime import datetime

def days_until_christmas():
    
    today = datetime.now().date()
    christmas = datetime(today.year, 12, 24).date()

    if today > christmas:
       christmas = datetime(today.year + 1, 12, 24).date()

    delta = christmas - today
    days = str(delta.days) + " days until Christmas!"
    return days


def handler(event, context):
    return {
        'statusCode': 200,
        'body':days_until_christmas()
    }