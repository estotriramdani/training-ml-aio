import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('best_log_model.pkl', 'rb') as file_1:
    best_model = pickle.load(file_1)

def run():
    # Create form for user input
    with st.form(key='form_parameters'):
        pid = st.number_input(
            'Product ID',
            min_value=1001,
            max_value=9999,
            value=1001,
            step=1,
            help='Enter the Product ID'
        )

        pcat = st.selectbox(
            'Product Category',
            ('Energy Drink', 'Water', 'Soda', 'Juice'),
            index=0
        )

        sales_volume = st.number_input(
            'Sales Volume (L)',
            min_value=0.0,
            value=0.0,
            step=0.1,
            help='Enter the sales volume in liters'
        )

        price_per_liter = st.number_input(
            'Price per Liter (IDR)',
            min_value=0.0,
            value=0.0,
            step=0.1,
            help='Enter the price per liter in IDR'
        )

        advertising_spend = st.number_input(
            'Advertising Spend (USD)',
            min_value=0.0,
            value=0.0,
            step=0.1,
            help='Enter the advertising spend in USD'
        )

        num_retailers = st.number_input(
            'Number of Retailers',
            min_value=0,
            value=1,
            step=1,
            help='Enter the number of retailers'
        )

        temperature = st.number_input(
            'Temperature (°C)',
            min_value=-50.0,
            max_value=50.0,
            value=25.0,
            step=0.1,
            help='Enter the temperature in Celsius'
        )

        market_share = st.number_input(
            'Market Share (%)',
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.1,
            help='Enter the market share percentage'
        )

        competitor_price = st.number_input(
            'Competitor Price per Liter (IDR)',
            min_value=0.0,
            value=0.0,
            step=0.1,
            help='Enter the competitor price per liter in IDR'
        )

        submitted = st.form_submit_button('Predict')

    if submitted:
        # Prepare the input data
        data_inf = pd.DataFrame([{
            'Product_ID': pid,
            'Sales_Volume_(L)': sales_volume,
            'Product_Category': pcat,
            'Price_per_Liter_(IDR)': price_per_liter,
            'Advertising_Spend_(USD)': advertising_spend,
            'Number_of_Retailers': num_retailers,
            'Temperature_(°C)': temperature,
            'Market_Share_(%)': market_share,
            'Competitor_Price_per_Liter_(IDR)': competitor_price,
        }])

        st.dataframe(data_inf)

        # Predict using the model
        y_pred_inf = best_model.predict(data_inf)
        st.write('# Rating:', str(y_pred_inf[0]))

if __name__ == '__main__':
    run()

