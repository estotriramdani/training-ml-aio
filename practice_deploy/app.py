# Import libraries
import eda, predict
import streamlit as st

# Add side bar
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Holiday Season Predictor'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write('''This tool is designed to explore and predict the holiday season for new product.''')

# Features
st.sidebar.write('''### Key Features:
- **Exploratory Data Analysis**: Analyze the data to uncover patterns and insights related to beverages product.
- **Holiday Season Predictor**: Use predictive models to forecast the likelihood of holiday season in products.''')

# Tools
st.sidebar.write('''### Tools Utilized:
- `Python`: For backend operations and model computations.
- `Streamlit`: For creating this interactive web application.
- `Scikit-learn`: For implementing machine learning models.''')

# Define the Home Page
def show_home():

    # Create title and introduction
    st.title('Welcome to Holiday Season Prediction Tool')
    st.write('''This tool is designed to explore and predict the holiday season for new product.''')

    # Add image
    st.image('https://www.aio.co.id/assets/images/about/amerta-building-564316f3b278f46f40e9f582b0bfc7a8.jpg',
            caption='Source: aio.co.id')

    st.markdown('---')

    # Dataset
    st.write('#### 📈 Dataset')
    st.markdown('''The dataset is ....''')

    # Problem Statement
    st.write('#### ⚠️ Problem Statement')
    st.markdown('''.....''')    

    # Objective
    st.write('#### 💡 Objective')
    st.markdown('''.....using ... model and metrics .... ''')

# Create condition to access different pages
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Holiday Season Predictor':
    predict.run()
