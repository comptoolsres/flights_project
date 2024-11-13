#!/usr/bin/env python

# Import the necessary modules
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Create a parser object
parser = argparse.ArgumentParser(description='Read and plot flight data')

# Add arguments
parser.add_argument('filename', type=str, help='the name of the CSV file to read')


# Parse the arguments
args = parser.parse_args()



# Read the data from the CSV file
df = pd.read_csv(args.filename)

# Using the Year and Month columns, calculate the number of flights each month
# Hint: Use the groupby() function
flights_per_month = df.groupby(['Year', 'Month']).size()
print(flights_per_month)

# Using the Year, Month and ArrDelay columns, calculate the number of flights delayed per month
# Hint: Use the groupby() function  
delayed_flights_per_month = df[df['ArrDelay'] > 0].groupby(['Year', 'Month']).size()
print(delayed_flights_per_month)