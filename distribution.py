import streamlit as st
import pandas as pd

# Dictionary to map month names to file paths
file_paths = {
    "January 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data January 2023.csv",
    "February 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data February 2023_0.csv",
    "March 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data March 2023_0.csv",
    "April 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data April 2023.csv",
    "May 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data May 2023.csv",
    "June 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data June 2023.csv",
    "July 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data July 2023.csv",
    "August 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data August 2023.csv",
    "September 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data September 2023.csv",
    "October 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data October 2023.csv",
    "November 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data November 2023.csv",
    "December 2023": r"C:\Users\proha\PycharmProjects\weather\TS Weather data December 2023.csv",
    "January 2024": r"C:\Users\proha\PycharmProjects\weather\TS Weather data January 2024.csv",
    "February 2024": r"C:\Users\proha\PycharmProjects\weather\TS Weather data February 2024.csv",
    "March 2024": r"C:\Users\proha\PycharmProjects\weather\TS Weather data March 2024.csv",
    "April 2024": r"C:\Users\proha\PycharmProjects\weather\TS Weather data April 2024(1).csv",
    "May 2024": r"C:\Users\proha\PycharmProjects\weather\TS Weather data May 2024(1).csv",
    "June 2024": r""
}


# Load data based on the selected month
def load_data(month):
    file_path = file_paths.get(month)
    if not file_path:
        st.error("This data will be available soon.")
        return None

    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%b-%y')
    data.index = data.index + 1  # Adjust index to start from 1
    return data

# Set the title of the app
st.title('Weather Data Visualization')

# Add the image above the "Select Month" section
st.sidebar.image(r"C:\Users\proha\PycharmProjects\weather\Swecha_Logo_English.png")

# Sidebar for month selection
st.sidebar.header('Select Month')
month = st.sidebar.selectbox('Month',
                             ["January 2023", "February 2023", "March 2023", "April 2023", "May 2023", "June 2023",
                              "July 2023", "August 2023", "September 2023", "October 2023", "November 2023",
                              "December 2023", "January 2024", "February 2024", "March 2024", "April 2024", "May 2024",
                              "June 2024"])

# Load the data for the selected month
weather_data = load_data(month)

if weather_data is not None:
    # Sidebar filters
    st.sidebar.header('Filters')
    districts = weather_data['District'].unique()
    selected_district = st.sidebar.selectbox('Select District', districts)
    mandals = weather_data[weather_data['District'] == selected_district]['Mandal'].unique()
    selected_mandal = st.sidebar.selectbox('Select Mandal', mandals)

    # Filter data based on selections
    filtered_data = weather_data[
        (weather_data['District'] == selected_district) & (weather_data['Mandal'] == selected_mandal)]

    # Display the filtered data
    st.write(f"## Data for {selected_mandal}, {selected_district} - {month}")
    st.write(filtered_data)

    # Plot temperature
    st.write(f"## Temperature in {selected_mandal}, {selected_district}")
    st.line_chart(filtered_data.set_index('Date')[['Min Temp (°C)', 'Max Temp (°C)']])

    # Plot humidity
    st.write(f"## Humidity in {selected_mandal}, {selected_district}")
    st.line_chart(filtered_data.set_index('Date')[['Min Humidity (%)', 'Max Humidity (%)']])

    # Plot wind speed
    st.write(f"## Wind Speed in {selected_mandal}, {selected_district}")
    st.line_chart(filtered_data.set_index('Date')[['Min Wind Speed (Kmph)', 'Max Wind Speed (Kmph)']])

else:
    st.error("Failed to load data.")
