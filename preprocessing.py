import re
import numpy as np
import pandas as pd
def preprocessor(data):

    date_time = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}:\d{2}\s(?:AM|PM)'

    text_message = re.split(date_time,data)
    #text_message = [message.strip().replace("[', ']", "") for message in text_message if message.strip()]
    text_messages = [message.strip() for message in text_message if message.strip()]
    cleaned_text_messages = [message.replace("[", "").replace("]", "").replace("'", "").replace(",", "") for message in text_messages][1:]



    dates = re.findall(date_time,data)

    df = pd.DataFrame({'user_messages':cleaned_text_messages,'message_date':dates})


    users=[]
    message=[]
    
    for m in df['user_messages']:
        splitted = re.split('([\w\W]+?):\s',m)
        if splitted[1:]:
            users.append(splitted[1])
            message.append(splitted[2])
        
        else:
            users.append('group_notification')
            message.append(splitted[0])
    df['user'] = users
    df['messages'] = message
    df.drop(columns=['user_messages'],inplace=True)

    df = pd.DataFrame({'users':users, 'user_message':message,'message_dates':dates})

    df['message_dates'] = pd.to_datetime(df['message_dates'],format = '%d/%m/%y, %H:%M:%S %p')



    
    
    df['month']= df['message_dates'].dt.month_name()
    df['year'] = df['message_dates'].dt.year
    df['day'] = df['message_dates'].dt.day
    df['minute'] = df['message_dates'].dt.minute
    df['hour'] = df['message_dates'].dt.hour
    df['month_number'] = df['message_dates'].dt.month
    df['date'] = df['message_dates'].dt.date
    df['day_name'] = df['message_dates'].dt.day_name()
    return df
