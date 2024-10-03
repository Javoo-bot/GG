#import all the libraries needed for the analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure Pandas to display all columns when printing a DataFrame and they will not be truncated.
pd.set_option("display.max_columns", None)  # None means all columns will be shown
pd.set_option("display.width", None)         # None means the output width will be set to unlimited

# Uploading data-set file with path attached
file_path = '/Users/lucapoldini/Desktop/progetti/Annual Greenhouse Gas (GHG) Air Emissions Accounts.csv'  # Specify the path of the CSV file
ghg_emissions = pd.read_csv(file_path)  # Read the CSV file and load the data into a DataFrame called ghg_emissions

# Display general information about the DataFrame
print("\n Info on DataFrame :")
ghg_emissions.info()  # Show a summary of the DataFrame, including the number of rows, columns, and data types

# Show the first 10 rows of the DataFrame
print("\n First 10 rows of Dataframe")
print(ghg_emissions.head(10))  # Display the first 10 rows of the DataFrame for an initial inspection of the data


