from datetime import datetime

def formatMessages(username, text):
    now  = datetime.now()
    info = {
        "username": username, 
        "text": text,
        "time": now.strftime("%d/%m/%Y %H:%M:%S")
    }
    return info