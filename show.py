from urlextract import URLExtract
import matplotlib.pyplot as plt      
import pandas as pd
from collections import Counter

def filtering(selected_user,df):

    if selected_user=='Overall':
        num_messages =  df.shape[0]

        words=[]

        for message in df['user_message']:
            words.extend(message.split())

        num_media = df[df['user_message']== '<Media omitted>\n>'].shape[0]

        links=[]
        extracting = URLExtract()
        for messages in df['user_message']:
            links.extend(extracting.find_urls(messages))

        return num_messages,len(words),num_media, len(links)

        

    else:
        
        latest_df =  df[df['users']==selected_user]
        num_messages = latest_df.shape[0]

        words=[]

        for message in latest_df['user_message']:
            words.extend(message.split())
        num_media = df[df['user_message']== '<Media omitted>\n>'].shape[0]

        links=[]
        extracting = URLExtract()
        for messages in latest_df['user_message']:
            links.extend(extracting.find_urls(messages))

        return num_messages,len(words),num_media,len(links)


def busy_number(df):
    count_user = df['users'].value_counts().head()
    df= round((df['users'].value_counts()/df.shape[0])*100,2).reset_index()
    return count_user,df

def most_common_words(selected_user,df):

    f= open("stopwords.txt",'r')
    stop_words = f.read()

    if selected_user!='Overall':
        df= df[df['users']==selected_user]

        tempo = df[df['users'] != 'group_notification']
        tempo = tempo[tempo['user_message'] != '<Media omitted>\n']

        words= []

        for message in tempo['user_message']:
            for word in message.lower().split():
                if word not in stop_words:
                    words.append(word)
        most_common_df= pd.DataFrame(Counter(words).most_common(20))
        return most_common_df





