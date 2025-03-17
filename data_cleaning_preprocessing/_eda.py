import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_dataset(df):
    print("="*50)
    print(f"Summary of {df}")
    print("="*50)
    
    print(f"Shape: {df.shape} (rows, columns)\n")
    print("Data Types:\n", df.dtypes, "\n")
    print("Missing Values:\n", df.isnull().sum(), "\n")
    print("Unique Values per Column:\n", df.nunique(), "\n")
    print("Descriptive Statistics:\n", df.describe(), "\n")
    print("First 10 Rows:\n", df.head(10), "\n")

def plot_categorical(df, categorical_columns, figsize=(10, 6), palette='Set2'):
    if isinstance(categorical_columns, str):
        categorical_columns = [categorical_columns]

    plt.figure(figsize=figsize)

    for i, col in enumerate(categorical_columns):
        plt.subplot(1, len(categorical_columns), i + 1)
        sns.countplot(data=df, x=col, palette=palette)
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def plot_numerical_histogram(df, numerical_columns, bins=20, figsize=(10, 6), color='skyblue'):
    if isinstance(numerical_columns, str):
        numerical_columns = [numerical_columns]

    # Set up the plot size
    plt.figure(figsize=figsize)

    for i, col in enumerate(numerical_columns):
        plt.subplot(1, len(numerical_columns), i + 1)
        sns.histplot(df[col], bins=bins, kde=True, color=color)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()