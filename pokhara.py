import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('./data/dhm-pokhara, nepal-air-quality.csv')[['date', ' pm25', ' pm10']]
df['date'] = pd.to_datetime(df['date'])
df[' pm25'] = pd.to_numeric(df[' pm25'], errors='coerce')
df[' pm10'] = pd.to_numeric(df[' pm10'], errors='coerce')

# Resample data to monthly frequency, calculating mean
monthly_mean = df.resample('M', on='date').mean()

# Create a figure and a set of subplots
fig, axs = plt.subplots(2)

# Plot data
axs[0].plot(monthly_mean.index, monthly_mean[' pm25'], label='PM2.5')
axs[1].plot(monthly_mean.index, monthly_mean[' pm10'], label='PM10')

# Set labels and title
axs[0].set(ylabel='PM2.5 Value', title='Monthly Average of PM2.5 over time')
axs[1].set(xlabel='Date', ylabel='PM10 Value', title='Monthly Average of PM10 over time')

# Set x-axis to show month and year for both subplots
months = mdates.MonthLocator()  # every month
months_fmt = mdates.DateFormatter('%b %Y')
for ax in axs:
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(months_fmt)

# Show the plot
plt.tight_layout()
plt.show()
