import streamlit as st
import pandas as pd
import os

# === Manually list your files ===
excel_files = [
    "TG Weather data May 2024 (2).csv",
    "TS Weather data April 2023.csv",
    "TS Weather data April 2024.csv",
    "TS Weather data August 2023.csv",
    "TS Weather data December 2023.csv",
    "TS Weather data February 2023_0.csv",
    "TS Weather data February 2024.csv",
    "TS Weather data January 2023.csv",
    "TS Weather data January 2024.csv",
    "TS Weather data July 2023.csv",
    "TS Weather data June 2023.csv",
    "TS Weather data March 2023_0.csv",
    "TS Weather data March 2024.csv",
    "TS Weather data May 2023.csv",
    "TS Weather data November 2023.csv",
    "TS Weather data October 2023.csv",
    "TS Weather data September 2023.csv",
    "TG Weather data May 2024.csv",
]

# === Folder containing your weather data files ===
data_dir = r"C:\Users\proha\PycharmProjects\Telangana-weather"

st.title("Telangana Weather Dashboard")

# === File selector ===
selected_file = st.selectbox("Select Weather Data File", sorted(excel_files))

if selected_file:
    file_path = os.path.join(data_dir, selected_file)

    try:
        # Load the file based on extension
        if selected_file.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)

        st.write(f"### Data Preview: {selected_file}")
        st.dataframe(df.head())

        st.write("### Summary Statistics")
        st.write(df.describe())

        # === Try to parse date column ===
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df = df.dropna(subset=['Date'])
            df = df.sort_values('Date')

            numeric_cols = df.select_dtypes(include='number').columns.tolist()

            for col in numeric_cols:
                if col != 'Date':
                    st.write(f"#### {col} Over Time")
                    st.line_chart(df.set_index('Date')[col])
        else:
            st.warning("⚠️ No 'Date' column found. Time-based plots will be skipped.")

    except Exception as e:
        st.error(f" Failed to read the file. Error: {e}")
