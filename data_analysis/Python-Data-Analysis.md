 Data Analysis with Python

# 1. Introduction

## 1.1 Intro to Data Analysis with Python

## 1.2 The Problem

### Why Data Analysis?

#### Data is everywhere

#### Data analysis / data science helps us answer questions from data

#### Data analysis plays an important role in

##### Discovering useful information

##### Answering questions

##### Predicting future or the unknown

## 1.3 Understanding the Data

### Dataset

## 1.4 Python Packages for Data Science

### Scientifics Computing Libraries

#### Pandas (Data Structures & Tools)

##### The primary instrument of Pandas is a 2-dimensional table consisting of column and row labels, which are called a DataFrame

#### NumPy (Arrays & Matrices)

#### SciPy (Integrals, Solving Differential Equations, Optimization)

### Visualization Libraries

#### Matplotlib (plots & graphs, most popular)

#### Seaborn (plots: heat maps, time series, violin plots)

### Algorithmic Libraries

#### Scikit-learn (Machine Learning: regression, classification ...)

##### built on NumPy, SciPy and Matplotlib

#### Statsmodels (Explore data, estimate statistical models, and perform statistical tests)

## 1.5 Importing and Exporting Data in Python

### Process of loading and reading data into Python from various resources

### Two important properties

#### Format

##### Format is the way data is encoded

#### File Path

##### tills us where the data is stored

### Importing a CSV into Python

#### In Pandas, the "read_csv()" method can read in files with columns separated by commas into a pandas DataFrame

##### import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url)

##### Read without headers: df = pd.read_csv(url, header = None)

##### Read with headers: first put header in a list, headers = ["1","2"...], then add df.columns=headers after read_csv

#### Printing the data frame

##### Show the first n rows: print(df.head(n))

##### Show the bottom n rows: print(df.tail(n))

#### Pandas support exporting to different formats in Python

##### csv

###### Read: df = pd.read_csv()

###### Save: df.to_csv()

##### json

###### Read: df = pd.read_json()

###### Save: df.to_json()

##### Excel

###### Read: df = pd.read_excel()

###### Save: df.to_excel()

##### sql

###### Read: df = pd.read_sql()

###### Save: df.to_sql()

## 1.6 Getting Started Analyzing Data in Python

# 2. Data Wrangling

## 2.1 Pre-Processing Data in Python

## 2.2 Dealing with Missing Values in Python

## 2.3 Data Formatting in Python

## 2.4 Data Normalization in Python

## 2.5 Binning in Python

## 2.6 Turning Categorical Variables into Quantitative Variables in Python

# 3. Exploratory Data Analysis

## 3.1 Exploratory Data Analysis

## 3.2 Descriptive Statistics

## 3.3. GroupBy in Python

## 3.4 Analysis of Variance ANOVA

## 3.5 Correlation

## 3.6 Correlation - Statistics

# 4. Model Development

## 4.1 Model Development

## 4.2 Linear Regression and Multiple Linear Regression

## 4.3 Model Evaluation Using Visualization

## 4.4 Polynomial Regression and Pipelines

## 4.5 Measures for In-Sample Evaluation

## 4.6 Prediction and Decision Making

# 5. Working with Data in Python

## 5.1 Model Evaluation and Refinement

## 5.2 Overfitting, Underfitting and Model Selection

## 5.3 Ride Regression

## 5.4 Grid Search
