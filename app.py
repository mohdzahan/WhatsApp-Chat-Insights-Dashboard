#Whatsapp Analyser

import streamlit as st
import pandas as pd
import preprocessing, show

import matplotlib.pyplot as plt
from io import StringIO



st.sidebar.title("Whatsapp Chats Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file:

    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = StringIO.read(stringio)

    df = preprocessing.preprocessor(string_data)



    user_list=df['users'].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")


    selected_user = st.sidebar.selectbox("Show Analysis Based On:",user_list)
    st.title('Top Statistics')

    if st.sidebar.button("Analyse"):
        number_of_messages,words,num_media,links = show.filtering(selected_user, df)
        
        column1 , column2 , column3, column4 = st.columns(4)
        
        with column1:
            st.metric(label="No. of Messages", value=number_of_messages)

        with column2:
            st.metric(label="Total Words", value=words)

        with column3:
            st.metric(label="Total Media", value=num_media)

        with column4:
            st.metric(label="Total Links", value=links)
        

        




        if selected_user == 'Overall':

            st.title("Most Usages in Month")
            timeline = show.monthy_timeline(selected_user , df)

            fig,ax = plt.subplots()
            ax.plot(timeline['time'],timeline['user_message'])
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)

            st.title("Most Active Users")
            busiest_users,new_df = show.busy_number(df)
            fig,ax = plt.subplots()
        



            ax.bar(busiest_users.index, busiest_users.values,color ='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)





        most_common_df = show.most_common_words(selected_user,df)        

        fig , ax = plt.subplots()

        
        ax.bar(most_common_df[0],most_common_df[1]) 
        plt.xticks(rotation='vertical')

        st.title('Most Common Words')
        st.pyplot(fig)  

        #daily timeline graph

        st.title("Daily Timeline")
        daily_timeline  =show.daily_timeline(selected_user,df)


        fig, ax =plt.subplots()
        ax.plot(daily_timeline['date'],daily_timeline['user_message'],color='green')
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig)


        st.title("Activity Map")

        coll1,coll2 = st.columns(2)

        with coll1:
            st.header("Most Busy Day")
            busy_day = show.activity_map(selected_user,df)

            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            st.pyplot(fig)

        with coll2:
            st.header("Most Busy Month")
            busy_month = show.activity_map_month(selected_user,df)

            fig,ax = plt.subplots()
            ax.bar(busy_month.index,busy_month.values)
            st.pyplot(fig)