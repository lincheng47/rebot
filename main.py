import streamlit as st
import pandas as pd
import numpy as np
# import datetime as dt


st.title('London Population Trend')

# DATE_COLUMN = 'year'
# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data
#
# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)
#
# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#
# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)

def load_data(data):
    # Create DataFrame
    df = pd.DataFrame(data)
    df['Year'] = df.Year.astype('int32')
    df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.year
    df = df.set_index('Year')
    return df

data_load_state = st.text('Loading data...')
data = load_data({
        'Year': list(range(2000, 2025)),
        'Population': [
            164300, 165700, 167100, 168500, 169900, 171300, 172700, 174100, 175500,
            176900, 178300, 185900, 188200, 190500, 192800, 195100, 197400, 199700,
            202000, 204300, 206600, 218900, 220300, 224407, 226000
        ]
    })
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw population data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of population by year')
st.line_chart(data)



# Data for average property prices in Barking and Dagenham
data_load_state2 = st.text('Loading data...')
data = load_data({
    'Year': [2000, 2005, 2010, 2015, 2020, 2023, 2024],
    'Average House Price': [100000, 150000, 200000, 270000, 350000, 377000, 380000],
    'Average Flat Price': [75000, 110000, 150000, 190000, 240000, 265000, 270000]
})
data_load_state2.text("Done! (using st.cache_data)")
if st.checkbox('Show raw property data'):
    st.subheader('Raw data')
    st.write(data)


col1, col2 = st.columns(2)

with col1:
    hdata = data[['Average House Price']]
    st.subheader('House price by year')
    st.bar_chart(hdata)

with col2:
    fdata = data[['Average Flat Price']]
    st.subheader('Flat price by year')
    st.bar_chart(fdata)


#
# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#
# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)

