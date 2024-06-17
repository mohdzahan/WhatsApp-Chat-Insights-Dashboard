#whatsapp Analyser

import streamlit as st
import pandas as pd
import preprocessing, show

import matplotlib.pyplot as plt
from io import StringIO



st.sidebar.title("Whatsapp Chats Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file:

    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)


    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)


    string_data = StringIO.read(stringio)
    # st.write(string_data)

    df = preprocessing.preprocessor(string_data)
    print(type(df))
    st.dataframe(df)

    user_list=df['users'].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")


    selected_user = st.sidebar.selectbox("Show Analysis Based On:",user_list)


    if st.sidebar.button("Analyse"):
        number_of_messages,words,num_media,links = show.filtering(selected_user, df)
        
        column1 , column2 , column3, column4 = st.columns(4)

        with column1:
            st.header("No. of Messages")
            st.title(number_of_messages)

        with column2:
            st.header("Total Words")
            st.title(words)

        with column3:
            st.header("Total Media")
            st.title(num_media)

        with column4:
            st.header("Total Links")
            st.title(links)

        if selected_user == 'Overall':
            st.title("Most Active Users")
            busiest_users,new_df = show.busy_number(df)
            fig,ax = plt.subplots()
        

            col1,col2 = st.columns(2)

            with col1:
                ax.bar(busiest_users.index, busiest_users.values,color ='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)


            with col2:
                st.dataframe(new_df)

        most_common_df = show.most_common_words(selected_user,df)           
        st.dataframe(most_common_df)
        

