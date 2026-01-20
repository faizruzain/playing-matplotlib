import matplotlib.pyplot as plt
import pandas as pd
import random

# Generating dummy data

traffic_data = {
    'date': '',
    'in (Kbps)': 0,
    'out (Kbps)': 0
}

traffic_data_df = pd.DataFrame(traffic_data, index=[0])

for row in range(31):
    for column in traffic_data_df.columns:
        if column == 'date':
            traffic_data_df.loc[row, column] = row + 1
        elif column == 'in (Kbps)':
            traffic_data_df.loc[row, column] = row+1*random.randint(1, 3) # random.expovariate()	+ 1
        elif column == 'out (Kbps)':
            traffic_data_df.loc[row, column] = row+1*random.randint(3, 5) # random.expovariate() + 2

print(traffic_data_df)
print('\n')

# Plotting Traffic Data

fig, ax = plt.subplots()
ax.plot('in (Kbps)', data=traffic_data_df, label='Traffic In')
ax.plot('out (Kbps)', data=traffic_data_df, label='Traffic Out')
legend = ax.legend(loc='upper left', shadow=True)

# Put a nicer background color on the legend.
legend.get_frame()

plt.ylabel('Kbps')
plt.xlabel('Date')
plt.show()

# print(f'Traffic in: {traffic_in}')
# print(f'Traffic out: {traffic_out}')

# print(traffic_data_df.get(['in (Kbps)']).iloc[0])
# print(traffic_data_df.get(['in (Kbps)']).iloc[0].iloc[0])