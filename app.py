import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Data Cleaner", layout="centered")

st.title("🧹 Automated CSV Data Cleaner")
st.write("Upload your messy CSV file below to remove duplicates and fix missing values instantly!")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())
    
    if st.button("Clean Data Now"):
        # Processing logic
        cleaned_df = df.drop_duplicates()
        cleaned_df = cleaned_df.fillna("N/A")
        
        st.success("Data cleaned successfully!")
        st.subheader("Cleaned Data Preview")
        st.dataframe(cleaned_df.head())
        
        # Download button
        csv_data = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned CSV",
            data=csv_data,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )
