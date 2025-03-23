# WhatsApp Chat Insights Dashboard

This project analyzes WhatsApp chat data to extract insights like the most active users, commonly used words, and media shared. It presents these findings in an interactive dashboard using **Streamlit**.

## Features

- **User Statistics**: Shows total messages, words, media shared, and links for each user.
- **Most Active Users**: Displays the most active users in the group chat.
- **Most Common Words**: Lists the top 20 most used words, with stopwords removed.
- **Monthly and Daily Timeline**: Visualizes message activity over time.
- **Activity Map**: Shows the most active days of the week and the busiest months.
- **Link and Media Extraction**: Extracts and counts links and media shared in the chat.

## Project Structure

```
.
├── preprocessing.py           # Contains functions for data preprocessing
├── show.py                    # Contains functions for showing visualizations
├── app.py                     # Main Streamlit app
├── _chat.txt                  # Sample WhatsApp chat export file
├── stopwords.txt              # List of stopwords used in filtering
└── README.md                  # This file

```

## How to Run

1.	Install the required libraries:
Make sure you have Python 3.x installed and use the following command to install the required libraries:
```
pip install streamlit matplotlib pandas urlextract
```

2.	Prepare WhatsApp Data:
   
	-	Export your WhatsApp chat (without media) and save it as a .txt file.

4.	Run the Streamlit App:
   
To start the application, run the following command in your terminal:

```
streamlit run app.py
```

4.	Upload Chat File:
	-	Once the app is running, upload the exported WhatsApp chat file using the file uploader on the sidebar.
5.	View Results:
	-	Select a specific user or choose “Overall” to view the analysis for the entire chat.
	-	Click the Analyze button to generate insights.


## Preprocessing and Data Analysis

### Data Cleaning

The chat data is cleaned by:

-	Extracting timestamps and separating user messages.
-	Handling group notifications and media messages like <Media omitted>.

## Visualizations

-	Most Active Users: Bar chart of the top users by message count.
<img width="1670" alt="image" src="https://github.com/user-attachments/assets/11a168ee-809d-427d-a713-6fc4d1cd1213">

-	Most Common Words: Bar chart of frequently used words, excluding stopwords.
<img width="1667" alt="image" src="https://github.com/user-attachments/assets/a15a1d5a-fac7-457f-8bac-f30b8228c0d3">

-	Activity Timeline: Line plot showing activity by month and by day.
<img width="1242" alt="image" src="https://github.com/user-attachments/assets/be1d62d6-8055-428e-bc80-759658ed4e3e">

  
-	Activity Map: Visualization of message activity based on days of the week and months.
<img width="1286" alt="image" src="https://github.com/user-attachments/assets/28993a45-4ea6-43b6-ae1b-81e984adb410">


### Dependencies

-	Python 3.x
-	Streamlit
-	Matplotlib
-	Pandas
-	URLExtract

### Example

Here’s an example of the dashboard:

-	Top Users by Messages
-	Monthly Timeline
-	Most Common Words


