import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

# read_csv by default with a header
# df = pd.read_csv(url)

# our dataset has no header, using below syntax
df = pd.read_csv(url, header = None)

# printing the dataframe
# df.head(n) to show the first n rows of data frame, while df.tail(n) show the bottom n rows
print(df.head(5))
print(df.tail(5))