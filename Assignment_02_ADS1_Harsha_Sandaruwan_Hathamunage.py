"""
Created on Mon Mar 27 21:05:43 2023

@author: Harsha Sandaruwan Hathamunage
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def process_data(url):
    """
    The function reads data from a CSV file at the provided URL and filters it
    based on desired indicators, countries, and years, resulting in two cleaned
    dataframes: df_years and df_countries.

    Args:
        - url (str): The URL of the CSV file to read.

    Returns:
        - df_years (pandas.DataFrame): A dataframe containing the filtered and
        cleaned data with selected years, countries and indicators.
        - df_countries (pandas.DataFrame): A dataframe containing the
        transposed and processed data with countries as columns.
    """

    # Read data from CSV file
    df = pd.read_csv(url, skiprows=4)

    # Define the list of South Asian countries
    south_asia = ['Afghanistan', 'Bangladesh', 'Bhutan',
                  'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Define the list of desired indicators
    desired_indicators = ['Total greenhouse gas emissions (kt of CO2 equivalent)',
                          'Arable land (% of land area)',
                          'Forest area (% of land area)',
                          'Average precipitation in depth (mm per year)']

    # Filter the original dataframe by countries list and desired indicators
    df_south_asia = df[(df['Country Name'].isin(south_asia)) & (
        df['Indicator Name'].isin(desired_indicators))]

    # Select the desired years and set them as columns
    years = ['2000', '2005', '2010', '2015', '2018']
    df_years = df_south_asia.loc[:, [
        'Country Name', 'Country Code', 'Indicator Name'] + years]

    # Remove rows with missing values
    df_years.dropna(inplace=True)

    # Reset the index
    df_years = df_years.reset_index(drop=True)

    # Transpose DataFrame without index
    df_countries = df_years.set_index('Country Name').transpose()

    return df_years, df_countries


# Dataset file
url = 'https://github.com/Harsha-hathamunage/ADS1---Assignment-2-Statistics-and-trends/raw/main/Climate%20Change%20Dataset.csv'

# Call the function with the URL argument
df_years, df_countries = process_data(url)

# Print the two resulting dataframes
print(df_years)
print(df_countries)
