import streamlit as st

# Function to display project details
def show_project_details(project_name):
    if project_name == "TALE - Context-based AI Speech Assistance":
        st.subheader('1. ' + project_name)
        st.write('The first context-based AI speech assistance for Aphasia Patient.')
        st.write('''Link to MVP: [TALE App](https://tale-app.azurewebsites.net/)''')
        st.image('Image/TALE2.png', use_column_width=True)
    
    # Add other projects here using elif
    elif project_name == "StockTalk - Stock Price Prediction":
        st.subheader('2. ' + project_name)
        st.write('A project that leverages sentiment analysis from news articles to predict stock market trends.')
        st.write('''Find demo: [StockTalk](https://www.youtube.com/watch?v=uSOzkcL-hZE)''')
        st.write('Example of the news sentiment analysis')
        st.image('Image/news.png', use_column_width=True)
        st.write('Example of the stock price prediction based on news sentiment analysis')
        st.image('Image/stock.png', use_column_width=True)
        # Add content for StockTalk
    
    elif project_name == "TidyTeddy - AI Cleaning Companion":
        st.subheader('3. ' + project_name)
        st.write('Tidy-Teddy transforms cleaning from a chore into a thrilling adventure for both adults and kids with real-time room analysis and image processing. ')
        st.write('''Find out more: [TidyTeddy](https://sites.google.com/uw.edu/yourcleaningcompanion/homepage)''')
        st.image('Image/Prototyping2.jpg', use_column_width=True)
        # Add content for TidyTeddy
    
    # Continue with elif blocks for other projects
    # ...

# Main title
st.title('Ghea Chrestella - Project Portfolio')

# About Me section
st.header('About Me')
st.write('''Passionate about product management, I bring over 7 years of expertise in financial technology, having contributed to leading firms like Gojek - Tokopedia, Sea Group, and OCBC Bank. My approach is deeply rooted in data-driven decision-making and innovative product development. Currently, I am advancing my skills as a Computer Science Graduate Student at the University of Washington.  
        ''')

# Links to LinkedIn and GitHub
st.markdown('Find out more about me on [LinkedIn](https://www.linkedin.com/in/suyonoghea/) and [GitHub](https://github.com/gheacs).')

# Sidebar for project navigation
st.sidebar.title('Projects')
project_names = ["Select a project", "TALE - Context-based AI Speech Assistance", "StockTalk - Stock Price Prediction", "TidyTeddy - AI Cleaning Companion", "SleepAid", "Simple Wearable Device"]
selected_project = st.sidebar.selectbox('Select a project to view details:', project_names)

# Main content area
if selected_project != "Select a project":
    show_project_details(selected_project)
else:
    # Highlights section
    st.header('Highlights')
    st.subheader('''Second Quarter is a Wrap! What's next?''')
    st.write('''My GitHub contributions are inversely proportional to my sleep duration; this quarter has been intense, but I've learned a lot.''')
    st.image('Image/Github.png', use_column_width=True)

    st.subheader('Tale advanced to the Hollomon Innovation Challenge 2024 Final')
    st.write('[Read more about the Hollomon Health Innovation Challenge 2024](https://blog.foster.uw.edu/biggest-hollomon-health-innovation-challenge-ever/)')
    st.image('Image/TALE.jpg', use_column_width=True)

    st.subheader('First Quarter Recap')
    st.write('''I'm incredibly proud of myself and grateful for the steep learning curve I've navigated over the past three months in the prototyping course.''')
    st.image('Image/Prototyping2.jpg', use_column_width=True)

# You can add more content below for the sections that are always visible regardless of sidebar selection
# ...
