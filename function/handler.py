from datetime import datetime

def handler(event, context):
    
    date1 = datetime.now().date()
    date2 = datetime(2023, 12, 24)
    delta = date2 - date1

    return {
        'statusCode': 200,
        'body': str(delta.days)
    }
