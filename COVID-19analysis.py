# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
from ipywidgets import interact

# Load COVID-19 data into a DataFrame (assuming you have a CSV file named 'covid_data.csv')
covid_data = pd.read_csv('covid_data.csv')

# Function to plot COVID-19 data based on country selection
def plot_covid_data(country, data_type):
    country_data = covid_data[covid_data['Country/Region'] == country]
    country_data_grouped = country_data.groupby('Date')[data_type].sum()
    
    plt.figure(figsize=(10, 6))
    plt.plot(country_data_grouped.index, country_data_grouped.values, marker='o', linestyle='-', color='b')
    plt.title(f'COVID-19 {data_type} Cases in {country}')
    plt.xlabel('Date')
    plt.ylabel(f'{data_type} Cases')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Get unique countries and data types in the dataset
countries = covid_data['Country/Region'].unique()
data_types = ['Confirmed', 'Deaths', 'Recovered']

# Create interactive widgets for selecting country and data type
country_selector = widgets.Dropdown(options=countries, description='Select Country:')
data_type_selector = widgets.Dropdown(options=data_types, description='Select Data Type:')

# Function to update plot based on widget selections
def update_plot(change):
    clear_output(wait=True)
    display(country_selector, data_type_selector)
    plot_covid_data(country_selector.value, data_type_selector.value)

# Attach the update_plot function to widget change events
country_selector.observe(update_plot, 'value')
data_type_selector.observe(update_plot, 'value')

# Display the interactive widgets and initial plot
display(country_selector, data_type_selector)
plot_covid_data(country_selector.value, data_type_selector.value)
