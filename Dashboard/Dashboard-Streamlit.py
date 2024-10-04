import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
sns.set(style='dark')

# Load the dataset
dataset = pd.read_csv("Dashboard/Bike_Sharing.csv")

# Sidebar
st.sidebar.title('Welcome!:sparkles:')
with st.sidebar:
    name = st.text_input('Please, enter your name ')
    if name:
        st.write(f"Hello, {name}. Have a nice day!")

# Title for the dashboard
st.title('🚲[Bike Sharing Dashboard]🚲')
st.header('Hi! This page is the bike rental count dashboard')

# Jumlah Pengguna
st.subheader('Trends in the Number of Users in 2011 and 2012')
dataset['mnth'] = pd.Categorical(dataset['mnth'], categories=
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'],
    ordered=True)
monthly_counts = dataset.groupby(by=["mnth", "yr"]).agg({"cnt": "mean"}).reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=monthly_counts,
    x="mnth",
    y="cnt",
    hue="yr",
    palette="bright",
    marker="o"
)

plt.xlabel(None)
plt.ylabel("Number of Users")
plt.legend(title="Year", loc="upper right")
plt.tight_layout()

st.pyplot(plt)

# Pengaruh musim
st.subheader('Seasonal Influence')
season_pattern = dataset.groupby('season')[['registered', 'casual']].sum().reset_index()

plt.figure(figsize=(8, 4))
bar_width = 0.4
x = np.arange(len(season_pattern['season']))
plt.bar(x - bar_width / 2, season_pattern['registered'], width=bar_width, label='Registered', color='tab:green')
plt.bar(x + bar_width / 2, season_pattern['casual'], width=bar_width, label='Casual', color='tab:blue')

plt.xlabel(None)
plt.ylabel('Number of Renters')
plt.title(None)
plt.xticks(x, season_pattern['season'])
plt.legend()
st.pyplot(plt)

# Pengaruh cuaca
st.subheader('Weather Influence')

plt.figure(figsize=(8, 4))
sns.barplot(
    x='weathersit',
    y='cnt',
    data=dataset,
    palette=['#DAA520', '#FFD700', '#DAA520'],
    ci=None
)
plt.title(None)
plt.xlabel(None)
plt.ylabel('Number of Renters')
st.pyplot(plt)

# Pengaruh hari libur
st.subheader('Holiday Influence')
plt.figure(figsize=(8,4))
sns.barplot(
    x='workingday',
    y='cnt',
    data=dataset,
    palette=['#DAA520','#FFD700'])

plt.title(None)
plt.xlabel(None)
plt.ylabel('Number of Renters')
st.pyplot(plt)

# Sebaran hari
st.subheader('Distribution of the number of rentals per day')
plt.figure(figsize=(8, 4))
sns.barplot(
    x='weekday',
    y='cnt',
    data=dataset,
    order=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
)

plt.title(None)
plt.xlabel(None)
plt.ylabel('Number of Renters')
st.pyplot(plt)

# Expander
with st.expander("View Analysis"):
    st.write(
        """
        - The trend of most bicycle use occurred in 2012 compared to 2011. The highest number of users in 2012 occurred in September, while in 2011 it occurred in June.
        - In the fall, the number of bicycle rentals is the highest. When entering the next season, winter, the number of bicycle rentals decreased slightly. In the spring, the number of rentals decreases drastically. Then the number increases again as we enter summer.
        - Weather conditions affect the number of bike rentals. When the weather is sunny, the number of rentals is the highest. This is followed by cloudy and rainy weather conditions, which have the lowest number of rentals.
        - The number of bike rentals increases every day during weekdays (Monday-Friday), which are working days. Then it decreases when entering the weekend and the lowest number of renters occurred on Sunday.
        - Weekdays are the time when most people rent bicycles. During holidays, the number of renters decreased.
        """
    )

st.caption("By: Muhammad Muthi' Nuritzan")
