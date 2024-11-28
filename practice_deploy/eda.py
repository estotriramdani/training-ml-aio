import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title ='Beverages - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Holiday season Prediction')

    # Membuat Sub Header
    st.subheader('EDA untuk Analis Dataset Beverages')

    # Menambahkan deskripsi
    st.write('Page ini dibuat oleh Vincent')
    st.write('# Halo')
    st.write('## Halo')
    st.write('### Halo')

    # Membuat garis lurus
    st.markdown('---')

    # Magic syntax
    '''
    Pada page kali ini, penulis akan melakukan eksplorasi sederhana,
    Dataset yang digunakan adalah dataset Beverages.
    '''

    # Show DataFrame
    df = pd.read_csv('https://raw.githubusercontent.com/Vincentim27/data/refs/heads/main/beverages.csv')
    st.dataframe(df)

    # Membuat Barplot
    st.write('#### Plot Procut Category')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Product Category',data=df)
    st.pyplot(fig)

    # Membuat Histogram berdasarkan input user
    st.write('#### Histogram berdasarkan Input User')
    pilihan = st.selectbox('Pilih kolom:',('Sales Volume (L)','Price per Liter (IDR)'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[pilihan], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Plotly Plot
    st.write('#### Plotly Plot - Temperature dengan Holiday season')
    #fig = px.scatter(df,x='...',y='...', hover_data=['id','volume'])
    fig = px.scatter(df,x=df['Temperature (°C)'],y=df['Holiday Season'], hover_data=['Temperature (°C)','Holiday Season'])
    st.plotly_chart(fig)

if __name__== '__main__':
    run()
