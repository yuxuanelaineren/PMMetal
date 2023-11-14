import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
dir_path = '/Users/renyuxuan/Desktop/2023/文章/南方文章/'
file_path = os.path.join(dir_path, '南方文章_数据', 'HealthRisk_Adults_Southern_forPython.xlsx')
df_Non = pd.read_excel(file_path, sheet_name='Non')
# df_Car = pd.read_excel(file_path, sheet_name='Car')

# Define the desired order for metals and cities
metal_Non_order = ["Cr", "Mn", "Co", "Ni", "As", "Cd"]
# metal_Car_order = ["Cr", "Co", "Ni", "As", "Cd", "Pb"]
city_order = ["Nanjing", "Mianyang", "Huangshi", "Nanchang", "Kunming", "Xiamen", "Guangzhou", "Wuzhishan"]
# type_order = ["Based on total contents", "Based on bioaccessible contents"]

# Create a custom order for metals using pd.Categorical
df_Non['Heavy metal(loid)'] = pd.Categorical(df_Non['Heavy metal(loid)'], categories=metal_Non_order, ordered=True)

# Create a custom order for cities using pd.Categorical
df_Non['City'] = pd.Categorical(df_Non['City'], categories=city_order, ordered=True)

# Pivot the DataFrame to have cities as columns, metals/types as rows
pivot_df = df_Non.pivot_table(index=['Heavy metal(loid)', 'City'], columns=['Type'], values='Health risk')

# ------------------------------------------------------------
# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# set front and front size for legend and title
plt.rcParams.update({'font.family': 'Arial', 'font.size': 12})

# Define colors for Bio and Total
colors = ['red', 'grey']

# Set the width of the bars
bar_width = 0.5

# Create a bar chart
bars = pivot_df.plot(kind='bar', width=bar_width, color=colors, ax=ax)

# Add black borders for each bar
for container in bars.containers:
    for bar in container:
        bar.set_edgecolor('black')
        bar.set_linewidth(0.5)

# Add labels and title
plt.xlabel("Heavy metal(loid)", fontname='Arial', fontsize=12)
plt.ylabel("Non-carcinogenic Health Risk", fontname='Arial', fontsize=12)
plt.yscale('log')  # Set the y-axis to log scale
plt.yticks(fontname='Arial', fontsize=12)
# Set x-axis ticks as only metals
# ax.set_xticklabels(pivot_df.index.get_level_values('City'))
# ax.tick_params(axis='x')

# Add vertical grids after each metal (every 8 bars)
for i in range(7, len(metal_Non_order) * len(city_order), 8):
    ax.axvline(x=i + 0.5, color='black', linestyle='--', linewidth=1)

# Add horizontal grids
# ax.axhline(y=1, color='black', linestyle='-', linewidth=0.5)

# legend
legend = ax.legend(loc='upper left')
legend.get_frame().set_linewidth(0.0)  # remove legend border
legend.get_frame().set_facecolor('white')  # Set legend background color to white
# Add a black border to legend symbols
for handle in legend.legendHandles:
    handle.set_edgecolor('black')
    handle.set_linewidth(0.5)

# Display the chart
plt.tight_layout()
plt.savefig("/Users/renyuxuan/Desktop/2023/文章/南方文章/南方文章_作图/南方作图_修改/HR_Adults_Non.tiff", format="TIFF", dpi=500)
plt.savefig("/Users/renyuxuan/Desktop/2023/文章/南方文章/南方文章_作图/南方作图_修改/HR_Adults_Non.eps", format="eps", dpi=500)
plt.show()

