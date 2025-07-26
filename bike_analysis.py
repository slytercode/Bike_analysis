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

