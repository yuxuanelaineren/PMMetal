import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings


# Load the Excel file
dir_path = '/Users/renyuxuan/Desktop/2022/文章/南方文章/'
file_path = os.path.join(dir_path, '南方文章_数据', 'MLR_Southern_forPython.xlsx')
df = pd.read_excel(file_path, sheet_name='Southern')

# Define the columns for data
cities = ["Nanjing", "Mianyang", "Huangshi", "Nanchang", "Kunming", "Xiamen", "Guangzhou", "Wuzhishan"]
metals = ["Cr", "Mn", "Co", "Ni", "Cu", "Zn", "As", "Cd", "Pb"]

# Define custom colors for the pie chart slices
custom_colors_rgb = [
    (34, 139, 34),     # Green for Traffic emissions
    (31, 61, 255),       # Dark Blue for Industrial emissions
    (139, 69, 19),     # Saddle Brown for Dust
    (6, 8, 8),         # Black for Coal combustion
    (205, 0, 0),       # Red for Oil combustion
    (84, 100, 100)    # Dark Gray for Others
]
# Convert RGB values to the range of 0.0 to 1.0
custom_colors_normalized = [(r / 255.0, g / 255.0, b / 255.0) for r, g, b in custom_colors_rgb]

# legend_labels = ["Traffic emissions", "Industrial emissions", "Dust", "Coal combustion", "Oil combustion", "Others"]

# Loop through each city
for city in cities:
    for metal in metals:
        # Filter the DataFrame for the current metal and city
        metal_city_df = df[(df['City'] == city) & (df['Heavy metal(loid)'] == metal)]

        # Check if there is data for this combination
        if not metal_city_df.empty:
            # Get the data for the current metal and city
            data = metal_city_df[["Traffic emissions", "Industrial emissions", "Dust", "Coal combustion", "Oil combustion", "Others"]].values[0]

            # Check for NaN values and replace them with zeros
            data = np.nan_to_num(data, nan=0.0)

            # Create the pie chart
            fig, ax = plt.subplots()
            ax.pie(data, labels=['', '', '', '', '', ''], autopct='', startangle=90, colors=custom_colors_normalized)
            # ax.set_title(f'{metal} in {city}')
            ax.axis('off')

            chart_name = f'pie_chart_{metal}_{city}.eps'
            plt.savefig(f'/Users/renyuxuan/Desktop/2022/文章/南方文章/南方文章_作图/南方作图_一改/MLR_pie_charts/{chart_name}', format="eps", dpi=500)

            # Display the plot
            plt.show()

            # Close the plot to free up resources
            plt.close(fig)

        else:
            # Issue a warning if no data is found
            warning_message = f"No data found for {metal} in {city}. Skipping..."
            warnings.warn(warning_message)