import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# create_user_count_df digunakan untuk menyiapkan user_count
def create_user_count_df(df):
    user_count = df[['date', 'casual', 'registered', 'total_count']]
    user_count = user_count[['date', 'casual', 'registered', 'total_count']].groupby('date').sum().reset_index()
    
    return user_count

# create_casual_and_regis_df digunakan untuk menyiapkan casual_regis_growth
def create_casual_and_regis_df(df):
    casual_regis_growth = df[['date', 'bln', 'casual', 'registered']]
    casual_regis_growth = casual_regis_growth[['date','bln', 'casual', 'registered']].groupby('date').sum().reset_index()
    
    return casual_regis_growth

# create_days_count_df digunakan untuk menyiapkan days_count
def create_days_count_df(df):
    days_count = df[['day', 'total_count']].groupby('day').sum().sort_values(by='day', ascending=False).reset_index()

    return days_count

# create_data_days_df digunakan untuk menyiapkan data_days
def create_data_days_df(df):
    data_days = df[['day','casual', 'registered']].groupby('day').sum().reset_index()

    return data_days

# create_casual_regis_days_growth digunakan untuk menyiapkan casual_regis_day_growth
def create_casual_regis_days_growth(df):
    casual_regis_day_growth = df[['year', 'casual', 'registered', 'day']]
    casual_regis_day_growth = casual_regis_day_growth[['day', 'casual', 'registered']].groupby('day').sum().reset_index()

    return casual_regis_day_growth

# create_season_df digunakan untuk menyiapkan season
def create_season_df(df):
    season = df[['musim', 'total_count']].groupby('musim').sum().sort_values(by='total_count', ascending=False).reset_index()

    return season

# create_cuaca_df digunakan untuk menyiapkan weather
def create_weather_df(df):
    weather = df[['cuaca', 'total_count']].groupby('cuaca').sum().sort_values(by='total_count', ascending=False).reset_index()

    return weather

# create_user_hour_df digunakan untuk menyiapkan user_hour
def create_user_hour_df(df):
    user_hour = df[['season', 'hour', 'total_count']]
    user_hour = user_hour[['hour', 'season', 'total_count']].groupby('hour').sum().reset_index()

    return user_hour

# load dataframe
all_df = pd.read_csv("all_data.csv")

# mengurutkan df berdasarkan date dan mengubah kolom menjadi datetime
datetime_columns = ["date"]
all_df.sort_values(by="date", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# membuat filter dengan widget date input serta menambahkan logo pada sidebar
min_date = all_df["date"].min()
max_date = all_df["date"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("bikesharelogo.png")

    # Mengambil start_date dan end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# data yang telah difilter disimpan di main_df
main_df = all_df[(all_df['date'] >= str(start_date)) &
                (all_df['date'] <= str(end_date))]

# memanggil helper function untuk visualisasi data
user_count = create_user_count_df(main_df)
casual_regis_growth = create_casual_and_regis_df(main_df)
days_count = create_days_count_df(main_df)
data_days = create_data_days_df(main_df)
casual_regis_day_growth = create_casual_regis_days_growth(main_df)
season = create_season_df(main_df)
weather = create_weather_df(main_df)
user_hour = create_user_hour_df(main_df)

#Melengkapi Dashboard dengan Berbagai Visualisasi Data
# menambahkan header
st.header('Bike Sharing System Dashboard :milky_way:')

# daily users
st.subheader('Daily Bike Sharing Users')

col1, col2, col3 = st.columns(3)

with col1:
    total_users = user_count.total_count.sum()
    st.metric("Total users", value=total_users)

with col2:
    total_casual_users = user_count.casual.sum()
    st.metric("Total casual users", value=total_casual_users)

with col3:
    total_registered_users = user_count.registered.sum()
    st.metric("Total registered users", value=total_registered_users)

fig= px.line(
        user_count,
        x="date",
        y="total_count",
        markers=True
    )

st.plotly_chart(fig, use_container_width=True)

# pertumbuhan casual dan registered users
st.subheader('Pertumbuhan Casual dan Registered Users')

fig= px.line(
        casual_regis_growth,
        x="date",
        y="registered",
        markers=True,
        title="Registered Users"
    )

st.plotly_chart(fig, use_container_width=True)

fig= px.line(
        casual_regis_growth,
        x="date",
        y="casual",
        markers=True,
        title="Casual Users"
    )

st.plotly_chart(fig, use_container_width=True)

# users berdasarkan hari
st.subheader('Registered dan Casual Users Berdasarkan Hari')

fig = go.Figure(data=[
    go.Bar(name='registered', x=data_days.day, y=data_days.registered),
    go.Bar(name='casual', x=data_days.day, y=data_days.casual)
    ])

fig.update_layout(
    barmode='group',
    #title='Perbandingan Jumlah Registered dan Casual Users'
    )
fig.update_xaxes(categoryorder='array', categoryarray=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

st.plotly_chart(fig, use_container_width=True)

# pengaruh musim dan cuaca
st.subheader('Pengaruh Musim dan Cuaca Terhadap Users')

col1, col2 = st.columns(2)

with col1:
    fig = px.pie(season, names='musim', values='total_count', hole=0.5)
    fig.update_traces(text=season['musim'], textposition='inside')
    fig.update_layout(showlegend=False, title='Persentase Users Berdasarkan Musim')

    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.pie(weather, names='cuaca', values='total_count', hole=0.5)
    fig.update_traces(text=weather['cuaca'], textposition='inside')
    fig.update_layout(showlegend=False, title='Persentase Users Berdasarkan Keadaan Cuaca')

    st.plotly_chart(fig, use_container_width=True)

# Pengaruh jam
st.subheader('Pertumbuhan Users Berdasarkan Waktu dalam Jam')

fig= px.line(
        user_hour,
        x="hour",
        y="total_count",
        markers=True,
        #title="Tingkat Penggunaan Bike-Sharing System Berdasarkan Jam"
    )
fig.update_xaxes(dtick=1, rangemode='normal', showticklabels=True)

st.plotly_chart(fig, use_container_width=True)
