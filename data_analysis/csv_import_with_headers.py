import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

# read_csv by default with a header
# df = pd.read_csv(url)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]

# our dataset has no header, using below syntax
df = pd.read_csv(url, header = None)
# repace the default header numberings
df.columns=headers

# printing the dataframe
# df.head(n) to show the first n rows of data frame, while df.tail(n) show the bottom n rows
# print(df.head(5))
# print(df.tail(5))

# Exporting a Pandas dataframe to CSV
# path = "c:\\temp\\automobile.csv"
# df.to_csv(path)

# In Pandas, we use dataframe.dtypes to check data types
# print(df.dtypes)

# Returns a statistical summary
# print(df.describe())
# print(df.describe(include="all"))

# dataframe.info() provides a concise summary of dataframe with showing the top 30 and bottom 30 rows of the DF
df.info()