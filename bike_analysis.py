import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('day.csv')
print(df.info())
print(df.describe())

# Map weekday numbers to names
weekday_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
avg_rentals = df.groupby('weekday')['cnt'].mean()
ax = avg_rentals.plot(kind='bar')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Average Number of Rentals')
ax.set_title('Average Bike Rentals by Day of the Week')
ax.set_xticklabels([weekday_names[i] for i in avg_rentals.index], rotation=45)
plt.tight_layout()
plt.show()

# Compare weekdays vs weekends
df['day_type'] = df['weekday'].apply(lambda x: 'Weekend' if x == 0 or x == 6 else 'Weekday')
avg_daytype = df.groupby('day_type')['cnt'].mean().reindex(['Weekday', 'Weekend'])
plt.figure(figsize=(6,4))
ax2 = avg_daytype.plot(kind='bar', color=['skyblue', 'orange'])
ax2.set_xlabel('Day Type')
ax2.set_ylabel('Average Number of Rentals')
ax2.set_title('Average Bike Rentals: Weekdays vs Weekend')
plt.tight_layout()
plt.show()