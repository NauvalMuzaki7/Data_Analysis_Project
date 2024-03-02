import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

#------------------

## Data Wrangling

### Gathering Data


day_df = pd.read_csv("day.csv")
day_df.head() #showing the 5 topmost data in file "day.csv"

hour_df = pd.read_csv("hour.csv")
hour_df.head() #showing the 5 topmost data in  file "hour.csv"


### Assessing Data

#provides detailed information about the DataFrame structure.
day_df.info()

#Checking if there are NAs in dataset
day_df.isna().sum()
#there is no missing value in "day_df"


#Showing the count of duplicate value
print("Duplicate Count: ", day_df.duplicated().sum())

#Showing some statistic descriptives of the data
day_df.describe()


#provides detailed information about the DataFrame structure.
hour_df.info()

#Checking if there are NAs in dataset
hour_df.isna().sum()
#there is no missing value in "day_df"


print("duplicate count: ", hour_df.duplicated().sum())

#Showing some statistic descriptives of the data
hour_df.describe()


#Change Data Type to Correct Type
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['season'] = day_df.season.astype('category')
day_df['mnth'] = day_df.mnth.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weathersit'] = day_df.weathersit.astype('category')


#Change the name of the nominal value on 'season' column
day_df.season.replace((1,2,3,4), ('Spring','Summer','Fall','Winter'), inplace=True)

#Change the name of the nominal value on 'Yr' column (0=2011, 1=2012)
day_df.yr.replace((0,1), (2011,2012), inplace=True)

#Change the name of the nominal value 'holiday'
day_df.holiday.replace((0,1), ('No', 'Yes'), inplace=True)

#Change the name of the nominal value on 'mnth'
day_df.mnth.replace((1,2,3,4,5,6,7,8,9,10,11,12),('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'), inplace=True)

#Change the name of the nominal value on 'weathersit'
day_df.weathersit.replace((1,2,3,4), ('Clear','Misty','Light_Snow','Heavy_Rain'), inplace=True)

#Change the name of the nominal value 'weekday'
day_df.weekday.replace((0,1,2,3,4,5,6), ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'), inplace=True)

#Change the name of the nominal value 'workingday'
day_df.workingday.replace((0,1), ('No', 'Yes'), inplace=True)

#Change name 'cnt' column to 'total'
day_df.rename(columns={'cnt': 'total'}, inplace=True)

day_df.info()


day_df.duplicated().sum()
#Checking duplicated data, and there are no duplicated data


day_df.isna().sum()
#Checking Missing value in data, and there are no missing value in data


day_df.describe()
#Checking Inaccurate value in the data, and all the values are normal


hour_df['dteday'] = pd.to_datetime(hour_df['dteday']) #Change Data type to Datetime
hour_df['season'] = hour_df.season.astype('category') #Change Data type to Categorical Variable (this is for ordered result in visualization)
hour_df['mnth'] = hour_df.mnth.astype('category') #Change Data type to Categorical Variable (this is for ordered result in visualization)
hour_df['holiday'] = hour_df.holiday.astype('category') #Change Data type to Categorical Variable (this is for ordered result in visualization)
hour_df['weekday'] = hour_df.weekday.astype('category') #Change Data type to Categorical Variable (this is for ordered result in visualization)
hour_df['workingday'] = hour_df.workingday.astype('category') #Change Data type to Categorical Variable (this is for ordered result in visualization)
hour_df['weathersit'] = hour_df.weathersit.astype('category') #Change Data type to Categorical Variable (this is for ordered result in visualization)


#Change the name of the nominal value on 'season' column
hour_df.season.replace((1,2,3,4), ('Spring','Summer','Fall','Winter'), inplace=True)

#Change the name of the nominal value on 'Yr' column (0=2011, 1=2012)
hour_df.yr.replace((0,1), (2011,2012), inplace=True)

#Change the name of the nominal value 'holiday'
hour_df.holiday.replace((0,1), ('No', 'Yes'), inplace=True)

#Change the name of the nominal value on 'mnth'
hour_df.mnth.replace((1,2,3,4,5,6,7,8,9,10,11,12),('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'), inplace=True)

#Change the name of the nominal value on 'weathersit'
hour_df.weathersit.replace((1,2,3,4), ('Clear','Misty','Light_Snow','Heavy_Rain'), inplace=True)

#Change the name of the nominal value 'weekday'
hour_df.weekday.replace((0,1,2,3,4,5,6), ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'), inplace=True)

#Change the name of the nominal value 'workingday'
hour_df.workingday.replace((0,1), ('No', 'Yes'), inplace=True)

#Change name 'cnt' column to 'total'
hour_df.rename(columns={'cnt': 'total'}, inplace=True)

hour_df.info()


hour_df.duplicated().sum()
#there are no duplicated data


hour_df.isna().sum()
#There are no missing values in the data


hour_df.describe()
#Checking Inaccurate value in the data, and all the values are normal


#Descriptive Statistics for Casual User, Registered User, and Total User
column_user = ["casual", "registered", "total"]
descriptive_stats = day_df[column_user].describe()

#Seeing the count of Casual User, registered User, and Total User based on Year
count_by_year = day_df.groupby('yr').agg({'casual': 'sum', 'registered': 'sum', 'total':'sum'})

#Seeing the average of Casual User, registered User, and Total User based on Year
mean_by_year = day_df.groupby('yr').agg({'casual': 'mean', 'registered': 'mean', 'total':'mean'})

#Seeing the count of Casual User, registered User, and Total User based on month
count_by_month = day_df.groupby('mnth').agg({'casual': 'sum', 'registered': 'sum', 'total':'sum'})

#Seeing the count of Casual User, registered User, and Total User based on weekday
count_by_weekday = day_df.groupby('weekday').agg({'casual': 'sum', 'registered': 'sum', 'total':'sum'})

#Seeing the average of Casual User, registered User, and Total User based on weekday
mean_by_weekday = day_df.groupby('weekday').agg({'casual': 'mean', 'registered': 'mean', 'total':'mean'})

#Seeing the count of Casual User, registered User, and Total User based on working day (1) or not working day (0)
count_by_workingday = day_df.groupby('workingday').agg({'casual': 'sum', 'registered': 'sum', 'total':'sum'})

#Seeing the average of Casual User, registered User, and Total User based on working day (1) or not working day (0)
mean_by_workingday = day_df.groupby('workingday').agg({'casual': 'mean', 'registered': 'mean', 'total':'mean'})

#Seeing the count of Casual User, registered User, and Total User based on weathersit (weather situation)
count_by_weathersit = day_df.groupby('weathersit').agg({'casual': 'sum', 'registered': 'sum', 'total':'sum'})

#Seeing the average of Casual User, registered User, and Total User based on weathersit (weather situation)
mean_by_weathersit = day_df.groupby('weathersit').agg({'casual': 'mean', 'registered': 'mean', 'total':'mean'})

#Seeing the average Casual User, registered User, and Total User based on Season
mean_by_season = day_df.groupby('season').agg({'casual': 'mean', 'registered': 'mean', 'total': 'mean'})

#Seeing the average Temperature and Wind Speed based on Season
day_df['temp_normal'] = day_df['temp']*41
day_df['atemp_normal'] = day_df['atemp']*50
day_df['windspeed_normal'] = day_df['windspeed']*67
mean_weather_season = day_df.groupby('season').agg({'temp_normal': 'mean', 'atemp_normal': 'mean', 'windspeed_normal': 'mean'})

##Hour Table
#Making Average of 3-way contingency table for Year, Season, Casual User, Registered User, And Total User
Table_3way_hour = hour_df.groupby(by=["yr", "season"]).agg({
    "casual": "mean",
    "registered": "mean",
    "total": "mean"
})




##-------- MAIN DASHBOARD --------##

#Add title to your dashboard
st.title('Bike Sharing Data Analysis Dashboard')
st.write('This dashboard is a powerful tool designed to provide comprehensive insights into bike sharing systems usage patterns and trends. This interactive dashboard leverages data visualization techniques to present key metrics and analytics in a user-friendly interface, catering to both casual users and data enthusiasts alike')
#Add subtitle
st.subheader('Data Analysis Project: Bike Sharing Dataset')

#Adding Line Chart Trend Bike Users 2011 dan 2012
### Pertanyaan 2: How is the monthly trend of the total bike users in 2011 and 2012?
st.subheader('')
st.subheader('Annual Trend of Total Bike Users in 2011 and 2012')
col1, col2 = st.columns(2)

with col1:
    result = day_df.groupby('yr').agg({'casual': 'sum', 'registered': 'sum', 'total':'sum'})
    total_2011 = result.loc[2011, 'total']
    st.metric("Total 2011 Users", value=total_2011)

with col2:
    total_2012 = result.loc[2012, 'total']
    st.metric("Total 2012 Users", value=total_2012)

#Split data into 2 years (2011 and 2012)
day_2011 = day_df[day_df['yr'] == 2011]
day_2012 = day_df[day_df['yr'] == 2012]

#seeing the count of Casual User, registered User, and Total User based on month for each years
monthly_trend_2011 = day_2011.groupby('mnth').agg({'casual': 'sum', 'registered': 'sum', 'total':'sum'})
monthly_trend_2012 = day_2012.groupby('mnth').agg({'casual': 'sum', 'registered': 'sum', 'total':'sum'})

#Create a new figure and axis
fig, ax = plt.subplots()

#Making Line Plot for year 2011 and 2012
ax.plot(monthly_trend_2011.index, monthly_trend_2011['total'], marker='o', label='2011', color='#00656B')
ax.plot(monthly_trend_2011.index, monthly_trend_2012['total'], marker='o', label='2012', color='#01C1CD')

#Add lable and title
ax.set_xlabel('Month')
ax.set_ylabel('Number of Users')
ax.set_title('Number of Total Users by Month')
ax.legend()

st.pyplot(fig)

#desc for line chart
st.write('Based on the line chart above, we can see that the trend of total bike users in 2011 is having uptrend until June, and having down after June to December. For total bike users in 2012 we can see that the trend is still indicating uptrend until September and have some sharp downtrend until December')

st.title('Descriptive Statistics and Aggregations')
st.subheader('Descriptive Statistics for Casual User, Registered User, and Total User')
st.table(descriptive_stats)


#Showing Total User by Years, Months, and Days Table

st.header('Table Based on Years, Months, and Days')

col1, col2 = st.columns(2)

with col1:
  st.subheader('Count of Users by Year')
  st.table(count_by_year)

with col2:
  st.subheader('Average of Users by Year')
  st.table(mean_by_year)


col1, col2 = st.columns(2)

with col1:
  st.subheader('Count of Users by Month')
  st.table(count_by_month)

with col2:
  st.subheader('Count of Users by Weekday')
  st.table(count_by_weekday)


st.subheader('Average of Users by Weekday')
st.table(mean_by_weekday)


#Showing table based on working day
st.header('Table Based on Working Day')
col1, col2 = st.columns(2)

with col1:
  st.subheader('Count of Users by Working Day')
  st.table(count_by_workingday)

with col2:
  st.subheader('Mean of Users by Working Day')
  st.table(mean_by_workingday)


#Showing table based on weather
st.header('Table Based on Weather and Season')
col1, col2 = st.columns(2)

with col1:
  st.subheader('Count of Users by Weather Situation')
  st.table(count_by_weathersit)

with col2:
  st.subheader('Mean of Users by Weather Situation')
  st.table(mean_by_weathersit)

col1, col2 = st.columns(2)

with col1:
  st.subheader('Mean of Users by Season')
  st.table(mean_by_season)

with col2:
  st.subheader('Mean Temperature, "Feels Like" Temperature, and Wind Speed by Season')
  st.table(mean_weather_season)


#3 Way Contingency Table Hour
st.header('Hourly Statistics by Year and Season')
st.table(Table_3way_hour)

st.header('')
###Showing 2011 and 2012 Boxplot
st.header('Distribution of Total Bike Users by Month')
col1, col2 = st.columns(2)

with col1:
  st.subheader('Boxplot of 2011')
  plt.figure(figsize=(15, 6))
  day_2011 = day_df[day_df['yr'] == 2011]

  #Make boxplot for 2011
  sns.boxplot(x='mnth', y='total', data=day_2011, color="#00656B")

  plt.xlabel('Month')
  plt.ylabel('Total Users')
  plt.title('Distribution of Total Bike Users by Month')

  #Show the plot in Streamlit
  fig, ax = plt.subplots()
  ax = sns.boxplot(x='mnth', y='total', data=day_2011, color="#00656B")
  st.pyplot(fig)

  st.write('From the boxplot above, we can see how the total number of bike users in 2011 is distributed and having some outliers in each month of the year, also the highest bike users is on June.')

with col2:
  st.subheader('Boxplot of 2012')

  plt.figure(figsize=(15, 6))

  #Filter data for the year 2011
  day_2012 = day_df[day_df['yr'] == 2012]

  #Make boxplot for 2011
  sns.boxplot(x='mnth', y='total', data=day_2012, color="#00656B")

  plt.xlabel('Month')
  plt.ylabel('Total Users')
  plt.title('Distribution of Total Bike Users by Month')

  #Show the plot in Streamlit
  fig, ax = plt.subplots()
  ax = sns.boxplot(x='mnth', y='total', data=day_2012, color="#01C1CD")
  st.pyplot(fig)

  st.write('From the boxplot above, we can see how the total number of bike users in 2012 is distributed and having some outliers in each month of the year, also the highest bike users is on September.')

st.header('')

###When Is The Best Time to Rent a Bike?
st.header(' ')
st.header('When Is The Best Time to Rent a Bike?')
st.subheader('Total of Monthly Data')

##Monthly data
#Determine the plot size
plt.figure(figsize=(12,5))

#Choosing the Color for bar plot
palette_colors = ["#00656B", "#01C1CD"]

#make the barplot with the color we choose
#Show the plot in Streamlit
fig, ax = plt.subplots()
ax = sns.barplot(x='mnth', y='total', data=day_df, hue='yr', palette=palette_colors)
st.pyplot(fig)

plt.xlabel("Month")
plt.ylabel("Total Users")
plt.title("Total of Bike Users per Month")

st.write('Based on the Bar plot above, we can see that the most total bike users in 2011 is on June and for the most total bike users in 2012 is on September')

##Seasonal data
st.subheader('Total of Seasonal Data')
#Determine the plot size
plt.figure(figsize=(12,5))

#Choosing the Color for bar plot
palette_colors = ["#00656B", "#01C1CD"]

#make the barplot with the color we choose
fig, ax = plt.subplots()
sns.barplot(x='season', y='total', data=day_df, hue='yr', palette=palette_colors)
st.pyplot(fig)

plt.xlabel("Season")
plt.ylabel("Total Rides")
plt.title("Total of bikeshare rides per Seasons")

st.write('Based on the year 2011 and 2012, both have the most users in Fall Season and have the least users in Spring Season.')

st.header('')

#Correlation Total and Weather
st.header('Correlation between Total Bike Users and The Weather')
col1, col2 = st.columns(2)

with col1:
  st.subheader('Correlation in 2011')
  #make data only in 2011
  day_2011 = day_df[day_df['yr'] == 2011]
  correlation = day_2011['total'].corr(day_2011['temp_normal'])

  fig, ax = plt.subplots()
  sns.scatterplot(x='total', y='temp_normal', data=day_2011)
  st.pyplot(fig)
  st.write('Based on the scatter plot above, we can see that while the total bike users is getting higher, the temperature is also getting higher. It means the correlation between total bike users and the temperature of the area has a positive correlation. Its supported by the high number of 0.77 indicates high positive correlation')

with col2:
  st.subheader('Correlation in 2012')
  #make data only in 2012
  day_2012 = day_df[day_df['yr'] == 2012]

  correlation = day_2012['total'].corr(day_2012['temp_normal'])

  fig, ax = plt.subplots()
  sns.scatterplot(x='total', y='temp_normal', data=day_2011)
  st.pyplot(fig)
  st.write('Based on the scatter plot above, we can see that while the total bike users is getting higher, the temperature is also getting higher. It means the correlation between total bike users and the temperature of the area has a positive correlation. Its supported by the high number of 0.71 indicates high positive correlation')


st.header('')
#Daily Total User
st.header('What Time That Has The Most of Total Bike Users?')

#Set the plot size
plt.figure(figsize=(15, 6))

#Split data into 2 years (2011 and 2012)
hour_2011 = hour_df[hour_df['yr'] == 2011]
hour_2012 = hour_df[hour_df['yr'] == 2012]

#seeing the count of Casual User, registered User, and Total User based on month for each years
daily_trend_2011 = hour_2011.groupby('hr').agg({'total':'mean'})
daily_trend_2012 = hour_2012.groupby('hr').agg({'total':'mean'})

#Making Line Plot for year 2011 and 2012
fig, ax = plt.subplots()
plt.plot(daily_trend_2011.index, daily_trend_2011['total'], marker='o', label='2011', color='#00656B')
plt.plot(daily_trend_2011.index, daily_trend_2012['total'], marker='o', label='2012', color='#01C1CD')
st.pyplot(fig)

#Add lable and title
plt.xlabel('Month')
plt.ylabel('Number of Users')
plt.title('Number of Total Daily Users')
plt.legend()

#Set x-axis ticks to show all values
plt.xticks(daily_trend_2011.index)

st.write('Based on the line chart above, we can see that the highest bike users in both years (2011 and 2012) are the same. It is in hour 17')

#Forecasting

st.header('Forecasting with Exponential Smoothing ')

#Define the function for Exponential Smoothing
def exponential_smoothing(data, alpha):
    forecasts = []
    forecasts.append(data[0])
    for t in range(1, len(data)):
        forecast = alpha * data[t] + (1 - alpha) * forecasts[t - 1]
        forecasts.append(forecast)
    return forecasts

alpha = 0.3

#Perform Exponential Smoothing and forecast for the next 2 days
def generate_forecast_plots(data):
    forecast_values = exponential_smoothing(data, alpha)
    last_observation = data[0]
    forecast_2_days = []
    for i in range(2):
        forecast = alpha * last_observation + (1 - alpha) * forecast_values[-1]
        forecast_2_days.append(forecast)
        last_observation = forecast_values[-1]

    #Plotting
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(data, label='Actual Data', color='#01C1CD')
    ax.plot(forecast_values, label='Forecast', color='#00656B')
    ax.set_xlabel('Time')
    ax.set_ylabel('Total')
    ax.set_title('Exponential Smoothing Forecasting for Total')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    #Display forecast for the next 2 days as a table
    forecast_table = pd.DataFrame({"Forecast": forecast_2_days})
    forecast_table.index += 1  # Start index from 1
    st.write("Forecast for the next 2 days:")
    st.table(forecast_table)

#Display the plots and forecast table in the Streamlit app
generate_forecast_plots(day_df['total'])

st.write('Based on the 2 time period of forecast above, we can see after december 2012 the trend of the total bike users tend to a bit uptrend. and the forecast pattern during following the actual data visually following the pattern.')














