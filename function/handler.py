from datetime import datetime

def handler(event, context):
    return {
        'statusCode': 200,
        'body': datetime.now().isoformat(),
        'h1': "Lasse er pen"
    }

